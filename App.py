import matplotlib
import seaborn
# from Connectors import IBMDB2Connector as db2
from Connectors import RobotTXTReader as rxml
from Connectors import SitemapXMLReader as sxml

def main():
    # query = "SELECT test_score as "+ "Test Score"+ ", count(*) as " + "Frequency" + " from INTERNATIONAL_STUDENT_TEST_SCORES GROUP BY test_score;"
    # dataframe = db2.generate_pdf(query)

    # dataframe = db2.generate_pdf(query).DataFrame()
    # plot = seaborn.barplot(x='Test Score', y='Frequency', data=dataframe)

    url = "https://lycia.org/"
    # url = rxml.generate_url("https://lycia.org/")
    # results = rxml.read_robots_file(url)
    # sitemap = rxml.find_sitemap(results)
    # dict = rxml.generate_dictionary(url)
    test = sxml.get_posts("https://lycia.org/sitemap.xml")
    print(test)
    # print(results)
    # print(sitemap)
    # print(dict)

if __name__ == "__main__":
    main()