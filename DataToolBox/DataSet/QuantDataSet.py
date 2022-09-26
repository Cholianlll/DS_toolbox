import DataSet

class QuantDataSet(DataSet.DataSet):
    def __init__(self,filename=None):
        '''Create a QualDataSet'''
        print('Creating a QualDataSet')
        super().__init__(filename)
        pass
    
if __name__ == '__main__':
    qual_data_set = QualDataSet()
    qual_data_set._DataSet__load()
    qual_data_set._DataSet__readFromCSV()
    qual_data_set.clean()
    qual_data_set.explore()