import ClassifierAlgorithm

class SimplekNNClassifier(ClassifierAlgorithm.ClassifierAlgorithm):
    def __init__(self,):
        super().__init__()
        print("SimplekNNClassifier.__init__()")
    
    def train(self,trainingSet = None):
        print("SimplekNNClassifier.train()")
        pass
    
    def test(self,trainingSet = None):
        print("SimplekNNClassifier.test()")
        pass
    
if __name__ == '__main__':
    test_classifier = SimplekNNClassifier()
    test_classifier.train()
    test_classifier.test()