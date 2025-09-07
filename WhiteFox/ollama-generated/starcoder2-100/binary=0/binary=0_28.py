
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        return v2


# Initializing the model with additional tensor as a keyword argument to `forward()` function of the model class:
other = torch.randn(3, 8, 49, 49)
m  = Model(other)

 # Inputs to the model and the additional tensor 
 x1  = torch.randn(250, 3, 64, 64) 
 
__output_1__  = m(x1)
 
