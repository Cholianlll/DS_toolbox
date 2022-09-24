class ClassifierAlgorithm(object):
    def __init__(self,dataset = None):
        '''Initialize the ClassifierAlgorithm'''
        self.dataset = dataset
        print('Initialize the ClassifierAlgorithm')
        pass
    def train(self,trainingSet = None):
        '''Train the ClassifierAlgorithm'''
        print('Train the ClassifierAlgorithm')
        pass
    def test(self,testingSet = None):
        '''Test the ClassifierAlgorithm'''
        print('Test the ClassifierAlgorithm')
        pass
    
if __name__ == '__main__':
    classifier = ClassifierAlgorithm()
    classifier.train()
    classifier.test()