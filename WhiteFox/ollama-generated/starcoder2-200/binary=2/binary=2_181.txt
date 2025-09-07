
class Model(torch.nn.Module):
    def __init__(self, v):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 5
        v2  = v1 - v # Subtract the output of the convolution from 'v' 
        return v2


# Initializing the model with a constant `5` for `other` in this case
m  = Model(5) 

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

