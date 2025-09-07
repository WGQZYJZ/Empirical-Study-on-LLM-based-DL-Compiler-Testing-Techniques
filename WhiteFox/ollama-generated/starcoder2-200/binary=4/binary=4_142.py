
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*8, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(64, 32*32*8)
other = torch.randn(64, 10) # The tensor added to the output of the linear transformation is different from the previous one.
__output__  = m(x)

