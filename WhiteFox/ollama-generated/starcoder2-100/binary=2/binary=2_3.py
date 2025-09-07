
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        return v1

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(256,3,960,480)
__output__  = m(x1)

