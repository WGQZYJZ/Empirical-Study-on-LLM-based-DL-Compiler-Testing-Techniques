
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,__input__):
        v0=self.__input__
        v1 = self.conv(v0)
        return torch.tanh(v1)


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(2,3,64,64)
