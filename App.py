import matplotlib
import seaborn
from Connectors import IBMDB2Connector as db2

def main():
    query = "SELECT test_score as "+ "Test Score"+ ", count(*) as " + "Frequency" + " from INTERNATIONAL_STUDENT_TEST_SCORES GROUP BY test_score;"
    dataframe = db2.generate_pdf(query)

    # dataframe = db2.generate_pdf(query).DataFrame()
    plot = seaborn.barplot(x='Test Score', y='Frequency', data=dataframe)



if __name__ == "__main__":
    main()