
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        return v1 + other 


# Initializing the model and providing a tensor as an argument for the additional parameter
other  = torch.randn(2, 8, 64, 64)
m  = Model(other=other)


# Inputs to the model
x1  = torch.randn(3, 3, 50, 70)
__output__  = m(x1)
