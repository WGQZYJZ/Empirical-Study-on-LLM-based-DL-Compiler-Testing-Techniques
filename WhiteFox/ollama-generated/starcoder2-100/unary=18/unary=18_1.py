
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v0 = x
        v1 = torch.sigmoid(v0) # apply sigmoid
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
__output__  = m(x1)
