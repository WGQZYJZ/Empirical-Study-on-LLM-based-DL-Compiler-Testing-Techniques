
class Model(torch.nn.Module):
    def __init__(self, other1, other2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1) # Apply pointwise convolution with kernel size 1 to the input tensor
        self._other1 = other1
        self._other2 = other2
 
    def forward(self, x1):
        v1  = self.conv(x1) - self._other1
        v2  = torch.nn.Tanh()(v1) * self._other2
        return v2


# Initializing the model
m1= Model(0.,5.) # Initialize a model with constant 'other' of 0 and another constant 'other2' of 5
m2= Model(torch.zeros_like(out),7.) #Initialize a model with constant 'other' of zeros initialized to the shape of out, other2 is set to 7


# Inputs to the model
x1 = torch.randn(1,3,64,64)
