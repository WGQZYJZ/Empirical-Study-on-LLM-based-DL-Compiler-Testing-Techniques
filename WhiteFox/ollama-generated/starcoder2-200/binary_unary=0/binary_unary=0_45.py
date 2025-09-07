
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v0  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v1  = v0 + other
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
other  = torch.randn(3,8,64,64)
x   = torch.randn(10, 3, 64, 64)
__output__  = m(x)

