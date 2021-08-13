"""Py Script to engage in making a connection with database and performing CRUD operations"""
import asyncpg
import asyncio
import traceback

class DataAccessor(object):
    """
    Creating a base class for all Database transactions
    """
    def __init__(self, username, password, database_name, hostname):
        try:
            self.username = username
            self.password = password
            self.database_name = database_name
            self.hostname = hostname
            self.loop = asyncio.new_event_loop()
        except Exception as ex:
            print(traceback.print_exc())

    async def fetchResults(self, query_statement):
        try:
            connection = await asyncpg.connect(user=self.username, password=self.password, database=self.database_name, host=self.hostname)
            stmt = await connection.prepare(query_statement)
            data = await stmt.fetch()
            return data
        except Exception as ex:
            print(traceback.print_exc())
        # else:
        #     print('The data brought by the query is:\n', data)
        finally:
            await connection.close()

    def execute(self, query_statement):
        try:
            data = self.loop.run_until_complete(self.fetchResults(query_statement=query_statement))
            for i in data :
                list_data = dict(i)
            # list_data = [dict(i) for i in data]
            return list_data
        except Exception as ex:
            print(traceback.print_exc())