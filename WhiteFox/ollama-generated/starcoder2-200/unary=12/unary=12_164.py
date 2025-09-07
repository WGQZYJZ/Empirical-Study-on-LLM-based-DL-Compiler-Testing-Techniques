class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = self.__getattribute__('conv')(x1)
        return self.__getattribute__('sigmoid')(v0) * self._get_module('conv')(v0),

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        return self.__getattribute__('sigmoid')(self._get_module('conv')(x1)) * v0
