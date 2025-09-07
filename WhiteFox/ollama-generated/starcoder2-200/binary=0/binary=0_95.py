
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.__keyword_argument__
        return v2


# Initializing the model with keyword argument "other"
m = Model()


# Inputs to the model using the keyword argument "other"
x1  = torch.randn(1, 3, 64, 64)
__output__= m(x1)