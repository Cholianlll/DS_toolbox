from . import DataSet


class TimeSeriesDataSet(DataSet):
    def __init__(self,filename=None):
        '''Initialize the TimeSeriesDataSet'''
        print('Initialize the TimeSeriesDataSet')
        super().__init__(filename)
        pass