
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.conv1(x1)
        return 0-v2
 


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 8, 64, 64) # Input tensor of shape 4 x 3 x 8 x 64 x 64.
__output__  = m(x1)

