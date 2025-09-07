
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is not None:
            self.__other__ = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        if hasattr(self, "__other__"): 
            v2  = v1 + self.__other__ 
        else: 
            return v1
# Initializing the model with some tensor "other" as a keyword argument to forward function
m_2 = Model()

