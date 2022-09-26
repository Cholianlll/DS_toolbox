#* test.py
#*
#*  ANLY 555 2022
#*  Project <Deliverable 1>
#*
#*  Due on: 2022-09-25
#*  Author(s): Chao Li
#*
#*
#*  In accordance with the class policies and Georgetown's
#*  Honor Code, I certify that, with the exception of the
#*  class resources and those items noted below, I have neither
#*  given nor received any assistance on this project other than
#*  the TAs, professor, textbook and teammates.
#*

import Toolbox as tbox

def testData():
    test = tbox.DataSet()
    test._DataSet__readFromCSV()
    test._DataSet__load()
    test.clean()
    test.explore()
    
def testQualDataSet():
    test = tbox.QualDataSet()
    test.readFromCSV()
    test.load()
    test.clean()
    test.explore()
    
def testQuantDataSet():
    test = tbox.QuantDataSet()
    test.readFromCSV()
    test.load()
    test.clean()
    test.explore()
    
def testTextDataSet():
    test = tbox.TextDataSet()
    test.readFromCSV()
    test.load()
    test.clean()
    test.explore()
    
def testTimeSeriesDataSet():
    test = tbox.TimeSeriesDataSet()
    test.readFromCSV()
    test.load()
    test.clean()
    test.explore()

def testClassifierAlgorithm():
    test = tbox.ClassifierAlgorithm()
    test.train()
    test.test()

def testSimplekNNClassifier():
    test = tbox.SimplekNNClassifier()
    test.train()
    test.test()
    
def testKdTreeKNNClassifier():
    test = tbox.KdTreeKNNClassifier()
    test.train()
    test.test()

def testExperiment():
    test = tbox.Experiment()
    test.runCrossVal()
    test.score()
    
    
    
if __name__ == '__main__':
    testData()
    testQualDataSet()
    testQuantDataSet()
    testTimeSeriesDataSet()
    testTextDataSet()
    
    
    testClassifierAlgorithm()
    testSimplekNNClassifier()
    testKdTreeKNNClassifier()
    
    testExperiment()
