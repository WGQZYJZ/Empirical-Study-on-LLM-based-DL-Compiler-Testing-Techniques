
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, oth): 
        v1 = self.linear_(x1)
        return torch.nn.functional.conv2d(v1, oth)

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 8 ,56 ,56)
other = 0.7
__output__= m(x1, other)

