
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        return v1 + self.__other__


# Initializing the model with the argument for other tensor
m  = Model()


# Inputs to the model (not passing the other tensor as a keyword argument to the forward function call)
x1  = torch.randn(1, 3, 64, 64)
 
 
