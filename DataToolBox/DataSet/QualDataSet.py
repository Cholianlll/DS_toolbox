import DataSet

class QualDataSet(DataSet.DataSet):
    def __init__(self,filename=None):
        '''Initialize the QualDataSet'''
        print('Initialize the QualDataSet')
        super().__init__(filename)
        pass
    
if __name__ == '__main__':
    qual_data_set = QualDataSet()
    qual_data_set._DataSet__load()
    qual_data_set._DataSet__readFromCSV()
    
