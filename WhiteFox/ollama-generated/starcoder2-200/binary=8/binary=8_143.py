
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + other


# Initializing the model
m = Model()
 
other = torch.randn(5, 7) # A tensor that is passed as a keyword argument to the addition operation.

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
__output__  = m(x1)

