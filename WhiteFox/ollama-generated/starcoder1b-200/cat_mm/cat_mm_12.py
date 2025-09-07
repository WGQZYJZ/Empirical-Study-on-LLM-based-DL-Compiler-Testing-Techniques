
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        y = torch.cat([x1, x2, ... , xN], 1) # Create an input tensor of dimension N
        return y


# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
y1  = torch.randn(3, 8, 32, 32)
