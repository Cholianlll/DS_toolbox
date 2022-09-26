#* Toolbox.py
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

##
# @mainpage Data Science ToolBox
#
# @section description_main Description
# An implementation of a data science toolbox in Python.
#
# @section notes_main Notes
# - Finished the Deliverable 1.

##
# @file Toolbox.py
#
# @brief Example Python program with Doxygen style comments.
#
# @section description_doxygen_example Description
# None
#
# @section libraries_main Libraries/Modules
# - None
#
# @section notes_doxygen_example Notes
# - None
#
# @section todo_doxygen_example TODO
# - None.
#
# @section author_doxygen_example Author(s)
# - Created by Chao Li on 2022-09-25.
# - Modified by Chao Li on 2022-09-26.
#

class DataSet():
    """Base class for all exceptions"""
    
    def __init__(self, filename = None):
        """Initialize the DataSet

        Args:
            filename (str, optional): The file needed to to loaded. Defaults to None.
        """
        print('Initialize the DataSet')
        pass
    def __readFromCSV(self, filename = None):
        """Private function to read from CSV file

        Args:
            filename (str, optional): Private function to read from CSV file. Defaults to None.
        """
        print('__readFromCSV function')
        pass
    
    def __load(self, filename = None):
        """Private function to load the DataSet

        Args:
            filename (str, optional): Private function to load the DataSet. Defaults to None.
        """
        print('__load function')
        pass
    
    def clean(self):
        """Clean the DataSet"""
        print('Clean the DataSet')
        pass
    
    def explore(self):
        """Explore the DataSet"""
        print('Explore the DataSet')
        pass
    


class QualDataSet(DataSet):
    """It is a private function to read quality data from CSV file

    Args:
        DataSet (class): It is the parent class of QualDataSet
    """
    def __init__(self,filename=None):
        """Initialize the QualDataSet

        Args:
            filename (str, optional): Restore the file name which will be read. Defaults to None.
        """
        print('Initialize the QualDataSet')
        super().__init__(filename)
        pass
    
    def readFromCSV(self,filename=None):
        """Read from CSV file

        Args:
            filename (str, optional): The name of CSV file. Defaults to None.
        """
        print('Read the QualDataSet from CSV')
        pass
    
    def load(self,filename=None):
        """Load the QualDataSet

        Args:
            filename (str, optional): The name of CSV file. Defaults to None.
        """
        print('Load the QualDataSet')
        pass

class QuantDataSet(DataSet):
    """Read quantity data from CSV file

    Args:
        DataSet (class): Parent class of QuantDataSet.
    """
    def __init__(self,filename=None):
        """Initialize the QuantDataSet

        Args:
            filename (str, optional): The file name of the dataset. Defaults to None.
        """
        print('Creating a QualDataSet')
        super().__init__(filename)
        pass
    
    def readFromCSV(self,filename=None):
        """Read from CSV file

        Args:
            filename (str, optional): Read csv from the file. Defaults to None.
        """
        print('Read the QuantDataSet from CSV')
        pass
    
    def load(self,filename = None):
        """Load the QuantDataSet

        Args:
            filename (str, optional): Load the data from the file. Defaults to None.
        """
        print('Load the QuantDataSet')
        pass
    
class TextDataSet(DataSet):
    """Read text data from CSV file

    Args:
        DataSet (class): Parent class of TextDataSet.
    """
    def __init__(self,filename=None):
        """Initialize the TextDataSet

        Args:
            filename (str, optional): File name. Defaults to None.
        """
        print('Creating a TextDataSet')
        super().__init__(filename)
        pass
    def readFromCSV(self,filename=None):
        """read from CSV file

        Args:
            filename (str, optional): File name. Defaults to None.
        """
        
        print('Read the TextDataSet from CSV')
        pass
    
    def load(self,filename=None):
        """load the TextDataSet

        Args:
            filename (str, optional): File name. Defaults to None.
        """
        print('Load the TextDataSet')
        pass
    
    

class TimeSeriesDataSet(DataSet):
    """Time series data set

    Args:
        DataSet (class): Parent class of TimeSeriesDataSet.
    """
    def __init__(self,filename=None):
        """Initialize the TimeSeriesDataSet

        Args:
            filename (str, optional): Data file name. Defaults to None.
        """
        print('Initialize the TimeSeriesDataSet')
        super().__init__(filename)
        pass
    
    def readFromCSV(self,filename=None):
        """read from CSV file

        Args:
            filename (str, optional): Data file name. Defaults to None.
        """
        print('Read the TimeSeriesDataSet from CSV')
        pass
    
    def load(self,filename=None):
        """load the TimeSeriesDataSet

        Args:
            filename (str, optional): Data file name. Defaults to None.
        """
        print('Load the TimeSeriesDataSet')
        pass
    
class ClassifierAlgorithm():
    """Parent class for all classifier algorithms
    """
    def __init__(self,dataset = None):
        """Initialize the ClassifierAlgorithm

        Args:
            dataset (pd.DataFrame, optional): The data stored in pandas DataFrame. Defaults to None.
        """
        self.dataset = dataset
        print('Initialize the ClassifierAlgorithm')
        pass
    def train(self,trainingSet = None):
        """train the ClassifierAlgorithm

        Args:
            trainingSet (pd.DataFrame, optional): Train the data. Defaults to None.
        """
        print('Train the ClassifierAlgorithm')
        pass
    def test(self,testingSet = None):
        """test the ClassifierAlgorithm

        Args:
            testingSet (pd.DataFrame, optional): Predicting with the model and test dataset. Defaults to None.
        """
        
        print('Test the ClassifierAlgorithm')
        pass


class SimplekNNClassifier(ClassifierAlgorithm):
    """Simple kNN classifier

    Args:
        ClassifierAlgorithm (class): Parent class of SimplekNNClassifier.
    """
    def __init__(self,):
        """Initialize the SimplekNNClassifier
        """
        super().__init__()
        print("SimplekNNClassifier.__init__()")
    
    def train(self,trainingSet = None):
        """Train the SimplekNNClassifier

        Args:
            trainingSet (pd.DataFrame, optional): Train the model. Defaults to None.
        """
        print("SimplekNNClassifier.train()")
        pass
    
    def test(self,testingSet = None):
        """Test the SimplekNNClassifier

        Args:
            testingSet(pd.DataFrame, optional): Predict with model and test dataset. Defaults to None.
        """
        print("SimplekNNClassifier.test()")
        pass    
    

class KdTreeKNNClassifier(ClassifierAlgorithm):
    """KdTree kNN classifier

    Args:
        ClassifierAlgorithm (class): Parent class of KdTreeKNNClassifier.
    """
    def __init__(self,):
        """Initialize the KdTreeKNNClassifier"""
        
        super().__init__()
        print("KdTreeKNNClassifier.__init__()")
    
    def train(self,trainingSet = None):
        """train the KdTreeKNNClassifier

        Args:
            trainingSet (pd.DataFrame, optional): Train the model. Defaults to None.
        """
        print("KdTreeKNNClassifier.train()")
        pass
    def test(self,trainingSet = None):
        """test the KdTreeKNNClassifier

        Args:
            trainingSet (pd.DataFrame, optional): predict with the model. Defaults to None.
        """
        
        print("KdTreeKNNClassifier.test()")
        pass

class Experiment():
    """Experiment class for outputing the result of the model"""
    def __init__(self,):
        """Initialize the Experiment"""
        print("Experiment.__init__()")
        pass
    
    def runCrossVal(self, k = None):
        """Run cross validation

        Args:
            k (int, optional): The number of slices for cross validation. Defaults to None.
        """
        print("Experiment.RunCrossVal()")
        pass
    
    def score(self):
        """Print the score of the model"""
        
        print("Experiment.score()")
        pass
    
if __name__ == '__main__':
    data = DataSet()
    data._DataSet__load()
    data._DataSet__readFromCSV()
    data.clean()
    data.explore()
