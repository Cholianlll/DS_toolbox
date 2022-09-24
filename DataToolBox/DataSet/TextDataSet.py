from . import DataSet

class TextDataSet(DataSet):
    def __init__(self,filename=None):
        '''Create a TextDataSet'''
        print('Creating a TextDataSet')
        super().__init__(filename)
        pass