
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): # Replace 3 by a non-constant value.
        v1 = self.conv(x1) 
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # Replace 3 by a non-constant value.
__output__  = m(x1)

