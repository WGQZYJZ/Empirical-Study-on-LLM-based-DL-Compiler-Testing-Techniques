
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other 
        return v2


# Initializing the model
m = Model()
other = Variable(torch.ones(v1.shape))
# Inputs to the model
x1 = torch.randn(3, 3)
 
# Initializing a variable
other = Variable(torch.ones(v1.shape))
__output__  = m(x1)
