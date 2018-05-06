from abc import ABC, abstractmethod

class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        '''返回折扣金额（正值）'''