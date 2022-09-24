class DataSet(object):
    def __init__(self, filename = None):
        '''Initialize the DataSet'''
        print('Initialize the DataSet')
        pass
    def __readFromCSV(self, filename = None):
        '''__readFromCSV function'''
        print('__readFromCSV function')
        pass
    
    def __load(self, filename = None):
        '''__load function'''
        print('__load function')
        pass
    
    def clean(self):
        '''Clean the DataSet'''
        print('Clean the DataSet')
        pass
    
    def explore(self):
        '''Explore the DataSet'''
        print('Explore the DataSet')
        pass
    
    
if __name__ == '__main__':
    data = DataSet()
    data._DataSet__load()
    data._DataSet__readFromCSV()
    data.clean()
    data.explore()