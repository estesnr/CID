import pyodbc
from datetime import datetime


class AccessAPI():

    def __init__(self):
        """
        Series of methods to interact with the maintenance access database.
        """
        self.access_path = "T:\\Manufacturing Records\\_RoRo Maintenace_PTR Tracking\\RORO.accdb"
        self.connection_str = f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={self.access_path};"

        self.connection = pyodbc.connect(self.connection_str)
        self.cursor = self.connection.cursor()

    def query_platforms(self):
        """
        Creates a dict that maps out the primary keys for different ROCC platforms to reference
        for other queries.
        """
        rows = {}

        try:
            self.cursor.execute(f"SELECT [Platform ID], [Platform Name] FROM Platform")

            for row in self.cursor.fetchall():
                rows[row[1]] = row[0]

        except Exception as e:
            raise RuntimeError(f"Error Retrieving Platform information: {e}")
            self.connection.close()

        return rows

    def get_current_maint_items(self, platform_name):
        """
        Retrieves a list of open maintenance items for a given platform.
        """

        platforms = self.query_platforms()

        for item in platforms:
            if item == platform_name.upper():
                platform_code = platforms[item]

        query = """
        SELECT Number, Title, [Problem Description], [Date Opened]
        FROM JobEntry
        WHERE [Platform Name] = ?
        AND [Ticket Status] = 'Open'
        """

        try:
            self.cursor.execute(query, (platform_code,))
            results_list = self.cursor.fetchall()
        except Exception as e:
            results = f"Connection Error: {e}"

        if not results_list:
            self.cursor.close()
            self.connection.close()
            return []
        else:
            results = [list(row) for row in results_list]
            for row in results:
                for item in row:
                    if isinstance(item, datetime):
                        index = row.index(item)
                        row[index] = item.strftime('%b-%d-%y')

            self.cursor.close()
            self.connection.close()
            return results

    def retrieve_maint_items(self):
        """
        Prompts user for input to locate current maintenance records for the
        desired platform. Formats the results into a more easily readable list.
        """
        platform = input('Enter Platform you wish to search for: \n')

        maint_items = self.get_current_maint_items(platform)

        self.cursor.close()
        self.connection.close()

        maint_list = []

        for item in maint_items:
            dict = {}
            dict['number'] = item[1]
            dict['entry'] = item[0]
            maint_list.append(dict)

        return maint_list
