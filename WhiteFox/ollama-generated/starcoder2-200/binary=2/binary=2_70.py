
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 - other
        return v2


# Initializing the model
m  = Model() 

# Inputs to the model
x   = torch.randn(3,64,64)

# Calculating output of the model
