import ibm_db
import pandas
import Credentials as cdt

dsn_hostname = cdt.ibm_db2["host"] # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = cdt.ibm_db2["username"]       # e.g. "abc12345"
dsn_pwd = cdt.ibm_db2["password"]     # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = cdt.ibm_db2["dsn"]
dsn_database = cdt.ibm_db2["db"]          # e.g. "BLUDB"
dsn_port = cdt.ibm_db2["port"]                # e.g. "50000"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)




def create_connection():
    try:
        conn = ibm_db.connect(dsn, "", "")
        print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
        close = ibm_db.close(conn)

    except:
        print("Unable to connect: ", ibm_db.conn_errormsg())

def create_table(table_name):
    drop_query = "drop table " + table_name

    try:
        conn = ibm_db.connect(dsn, "", "")
        print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
        drop_table = ibm_db.exec_immediate(conn, drop_query)
        # create_table = ibm_db.exec_immediate(conn, create_query) TODO: Create queries
        close = ibm_db.close(conn)
    except:
        print("Unable to connect: ", ibm_db.conn_errormsg())
        print("Unable to connect: ", ibm_db.stmt_errormsg())

def insert_data(select_query):
    try:
        conn = ibm_db.connect(dsn, "", "")
        select_inserted = ibm_db.exec_immediate(conn, select_query)
        while ibm_db.fetch_row(select_inserted) != False:
            print(" ID:", ibm_db.result(select_inserted, 0), " FNAME:", ibm_db.result(select_inserted, "FNAME"))
        close = ibm_db.close(conn)
    except:
        print("Unable to connect: ", ibm_db.stmt_errormsg())

## Convert query to DataFrame
def generate_pdf(query):
    import ibm_db_dbi
    try:
        conn = ibm_db.connect(dsn, "", "")
        pconn = ibm_db_dbi.Connection(conn)
        pdf = pandas.read_sql(query, pconn)
        all_df = pdf
        print(all_df)
        meta_df = pdf.shape
        print(meta_df)
        close = ibm_db.close(conn)
        return pdf

    except:
        print("Unable to connect: ", ibm_db.stmt_errormsg())

def execute_query(query):
    try:
        conn = ibm_db.connect(dsn, "", "")
        run_query = ibm_db.exec_immediate(conn, query)
        result = ibm_db.fetch_both(run_query)
        while ibm_db.fetch_row(result   ) != False:
            print(result[0])
            result = ibm_db.result(run_query, 0)
        close = ibm_db.close(conn)
    except:
        print("Unable to run the query: ", ibm_db.stmt_errormsg()) # Returns query error messages