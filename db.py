import sqlite3
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WarehouseDBHandler:

    def __init__(self, db_name='warehouse_management.db'):
        try:
            self.db = sqlite3.connect(db_name)
            self.create_tables()
            logger.info('Connected to database')
        except Exception as e:
            logger.error(f'Error while connecting to the database: {e}')

    def create_tables(self):
        try:
            self.db.execute('''CREATE TABLE IF NOT EXISTS Customer (
                                customer_id INTEGER PRIMARY KEY,
                                customer_name TEXT,
                                date TEXT
                            );''')

            self.db.execute('''CREATE TABLE IF NOT EXISTS Defined_Products (
                                product_id INTEGER PRIMARY KEY,
                                product_name TEXT,
                                raw_materials BLOB
                            );''')

            self.db.execute('''CREATE TABLE IF NOT EXISTS Raw_Materials (
                                raw_material_id INTEGER PRIMARY KEY,
                                raw_material_name TEXT,
                                quantity INTEGER
                            );''')

            self.db.execute('''CREATE TABLE IF NOT EXISTS Employee (
                                employee_id INTEGER PRIMARY KEY,
                                employee_name TEXT,
                                date TEXT
                            );''')

            self.db.execute('''CREATE TABLE IF NOT EXISTS Finished_Products (
                                finished_product_id INTEGER PRIMARY KEY,
                                artical_number INTEGER,
                                artical_name TEXT,
                                production_date TEXT,
                                best_before TEXT,
                                batch_number TEXT,
                                quantity INTEGER,
                                producing_employee TEXT,
                                raw_material BLOB,
                                special_feature TEXT
                            );''')

            self.db.execute('''CREATE TABLE IF NOT EXISTS Delivered_Products (
                                artical_number INTEGER PRIMARY KEY,
                                artical_name TEXT,
                                production_date TEXT,
                                best_before TEXT,
                                batch_number TEXT,
                                quantity INTEGER,
                                producing_employee TEXT,
                                raw_material BLOB,
                                special_feature TEXT
                            );''')

            self.db.commit()
            logger.info('Tables created successfully')

        except Exception as e:
            logger.error(f'Error while creating tables: {e}')

    # customer CRUD
    
    def insert_customer(self, customer_name, date):
        try:
            self.db.execute("INSERT INTO Customer (customer_name, date) VALUES (?, ?)",
                            (customer_name, date))
            self.db.commit()
            logger.info('Customer record created successfully')
        except Exception as e:
            logger.error(f'Error while creating customer record: {e}')

    def get_all_customers(self):
        try:
            cursor = self.db.execute("SELECT * FROM Customer")
            customers = cursor.fetchall()
            cursor.close()
            return customers
        except Exception as e:
            logger.error(f'Error while retrieving customers: {e}')
            return None

    def update_customer(self, customer_id, customer_name, date):
        try:
            q = "UPDATE Customer SET customer_name=?, date=? WHERE customer_id=?"
            self.db.execute(q, (customer_name, date, customer_id))
            self.db.commit()
            logger.info('Customer record updated successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to update customer record: {e}')
            return False

    def delete_customer(self, customer_id):
        try:
            q = "DELETE FROM Customer WHERE customer_id=?"
            self.db.execute(q, (customer_id,))
            self.db.commit()
            logger.info('Customer record deleted successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to delete customer record: {e}')
            return False
    

    # defined products CRUD
        
    def insert_defined_product(self, product_name, raw_materials):
        try:
            raw_material_blob = bytes(json.dumps([raw_materials]),'utf-8')
            self.db.execute("INSERT INTO Defined_Products (product_name, raw_materials) VALUES (?, ?)",
                            (product_name, raw_material_blob))
            self.db.commit()
            logger.info('Defined product record created successfully')
        except Exception as e:
            logger.error(f'Error while creating defined product record: {str(e)}')

    def get_all_defined_products(self):
        try:
            cursor = self.db.execute("SELECT * FROM Defined_Products")
            defined_products = cursor.fetchall()
        
            cursor.close()
            return defined_products
        except Exception as e:
            logger.error(f'Error while retrieving defined products: {e}')
            return None

    def get_defined_products_blob(self,product_id):
        try:
            q = "SELECT raw_materials FROM Defined_Products WHERE product_id=?"
            cursor = self.db.execute(q, (product_id,))
            defined_product_blob = cursor.fetchone()
            
            cursor.close()
            prev_data = json.loads(defined_product_blob[0].decode('utf-8'))
            print(prev_data)
            return prev_data
        except Exception as e:
            logger.error(f'Error while retrieving defined products: {e}')
            return None

    def get_defined_products_ids(self):
        try:
            cursor = self.db.execute("SELECT product_id, product_name FROM Defined_Products")
            products = cursor.fetchall()

            resultant_list = [] # list having names and ids merged : ['Junaid Nazir:2']
            if products:
                for i in products:
                    resultant_list.append(i[1]+f':{i[0]}')

            cursor.close()
            return resultant_list
        except Exception as e:
            logger.error(f'Error while retrieving defined products: {e}')
            return None


    def update_defined_product(self, product_id, product_name, raw_materials):
        try:
            q = "UPDATE Defined_Products SET product_name=?, raw_materials=? WHERE product_id=?"
            self.db.execute(q, (product_name, raw_materials, product_id))
            self.db.commit()
            logger.info('Defined product record updated successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to update defined product record: {e}')
            return False

    def update_defined_product_blob(self,product_id,raw_materials):
        try:
            raw_material_blob = bytes(json.dumps(raw_materials),'utf-8')
            q = "UPDATE Defined_Products SET raw_materials=? WHERE product_id=?"
            self.db.execute(q, (raw_material_blob, product_id))
            self.db.commit()
            logger.info('Defined product record updated successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to update defined product record: {e}')
            return False

    def delete_defined_product(self, product_id):
        try:
            q = "DELETE FROM Defined_Products WHERE product_id=?"
            self.db.execute(q, (product_id,))
            self.db.commit()
            logger.info('Defined product record deleted successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to delete defined product record: {e}')
            return False
    
    
    # Raw Materials CRUD
        
    def insert_raw_material(self, raw_material_name, quantity):
        try:
            self.db.execute("INSERT INTO Raw_Materials (raw_material_name, quantity) VALUES (?,?)", (raw_material_name,quantity,))
            self.db.commit()
            logger.info('Raw material record created successfully')
        except Exception as e:
            logger.error(f'Error while creating raw material record: {str(e)}')

    def get_all_raw_materials(self):
        try:
            cursor = self.db.execute("SELECT * FROM Raw_Materials")
            raw_materials = cursor.fetchall()
            cursor.close()
            return raw_materials
        except Exception as e:
            logger.error(f'Error while retrieving raw materials: {e}')
            return None

    def get_all_raw_materials_ids(self):
        try:
            cursor = self.db.execute("SELECT raw_material_id , raw_material_name FROM Raw_Materials")
            raw_materials = cursor.fetchall()

            resultant_list = [] # list having names and ids merged : ['Junaid Nazir:2']
            if raw_materials:
                for i in raw_materials:
                    resultant_list.append(i[1]+f':{i[0]}')

            cursor.close()
            return resultant_list
        except Exception as e:
            logger.error(f'Error while retrieving raw materials: {e}')
            return None
        
    def update_raw_material(self, raw_material_id, quantity):
        try:
            q = "UPDATE Raw_Materials SET quantity=? WHERE raw_material_id=?"
            self.db.execute(q, (quantity, raw_material_id))
            self.db.commit()
            logger.info('Raw material record updated successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to update raw material record: {e}')
            return False

    def delete_raw_material(self, raw_material_id):
        try:
            q = "DELETE FROM Raw_Materials WHERE raw_material_id=?"
            self.db.execute(q, (raw_material_id,))
            self.db.commit()
            logger.info('Raw material record deleted successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to delete raw material record: {e}')
            return False
        
    
    # Employee CRUD
    def insert_employee(self, employee_name, date):
        try:
            self.db.execute("INSERT INTO Employee (employee_name, date) VALUES (?, ?)",
                            (employee_name, date))
            self.db.commit()
            logger.info('Employee record created successfully')
        except Exception as e:
            logger.error(f'Error while creating employee record: {e}')

    def get_all_employees(self):
        try:
            cursor = self.db.execute("SELECT * FROM Employee")
            employees = cursor.fetchall()
            cursor.close()
            return employees
        except Exception as e:
            logger.error(f'Error while retrieving employees: {e}')
            return None

    def update_employee(self, employee_id, employee_name, date):
        try:
            q = "UPDATE Employee SET employee_name=?, date=? WHERE employee_id=?"
            self.db.execute(q, (employee_name, date, employee_id))
            self.db.commit()
            logger.info('Employee record updated successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to update employee record: {e}')
            return False

    def delete_employee(self, employee_id):
        try:
            q = "DELETE FROM Employee WHERE employee_id=?"
            self.db.execute(q, (employee_id,))
            self.db.commit()
            logger.info('Employee record deleted successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to delete employee record: {e}')
            return False
    

    # Finished_Products CRUD
        
    def insert_finished_product(self, artical_number, artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature):
        try:
            self.db.execute("INSERT INTO Finished_Products (artical_number, artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (artical_number, artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature))
            self.db.commit()
            logger.info('Finished product record created successfully')
        except Exception as e:
            logger.error(f'Error while creating finished product record: {e}')

    def get_all_finished_products(self):
        try:
            cursor = self.db.execute("SELECT * FROM Finished_Products")
            finished_products = cursor.fetchall()
            cursor.close()
            return finished_products
        except Exception as e:
            logger.error(f'Error while retrieving finished products: {e}')
            return None

    def update_finished_product(self, artical_number, artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature):
        try:
            q = "UPDATE Finished_Products SET artical_name=?, production_date=?, best_before=?, batch_number=?, quantity=?, producing_employee=?, raw_material=?, special_feature=? WHERE artical_number=?"
            self.db.execute(q, (artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature, artical_number))
            self.db.commit()
            logger.info('Finished product record updated successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to update finished product record: {e}')
            return False

    def delete_finished_product(self, artical_number):
        try:
            q = "DELETE FROM Finished_Products WHERE artical_number=?"
            self.db.execute(q, (artical_number,))
            self.db.commit()
            logger.info('Finished product record deleted successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to delete finished product record: {e}')
            return False
    
    # Delivered_Products CRUD
    def insert_delivered_product(self, artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature):
        try:
            self.db.execute("INSERT INTO Delivered_Products (artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature))
            self.db.commit()
            logger.info('Delivered product record created successfully')
        except Exception as e:
            logger.error(f'Error while creating delivered product record: {e}')

    def get_all_delivered_products(self):
        try:
            cursor = self.db.execute("SELECT * FROM Delivered_Products")
            delivered_products = cursor.fetchall()
            cursor.close()
            return delivered_products
        except Exception as e:
            logger.error(f'Error while retrieving delivered products: {e}')
            return None

    def update_delivered_product(self, artical_number, artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature):
        try:
            q = "UPDATE Delivered_Products SET artical_name=?, production_date=?, best_before=?, batch_number=?, quantity=?, producing_employee=?, raw_material=?, special_feature=? WHERE artical_number=?"
            self.db.execute(q, (artical_name, production_date, best_before, batch_number, quantity, producing_employee, raw_material, special_feature, artical_number))
            self.db.commit()
            logger.info('Delivered product record updated successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to update delivered product record: {e}')
            return False

    def delete_delivered_product(self, artical_number):
        try:
            q = "DELETE FROM Delivered_Products WHERE artical_number=?"
            self.db.execute(q, (artical_number,))
            self.db.commit()
            logger.info('Delivered product record deleted successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to delete delivered product record: {e}')
            return False
    
