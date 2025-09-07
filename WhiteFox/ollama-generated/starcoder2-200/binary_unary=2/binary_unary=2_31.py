

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 - other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
other = torch.ones(1, 8, 56, 56).to('cuda') # Generate a scalar or a tensor to represent "other" in this pattern

# Inputs to the model
x1  = torch.randn(1, 3, 50, 50)
__output__   = m(x1)

