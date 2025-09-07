
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v3  = v1 * negative_slope 
        v4  = torch.where(v2, v1, v3) # This is a typical pattern for implementing the Leaky ReLU activation function in a neural network
        return v4

# Initializing the model
m  = Model()
negative_slope  =  0.01568627450980392

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

