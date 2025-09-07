
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + v0 # Add v0 to the output of the convolution
        return v2


# Initializing the model with the input tensor passed as a keyword argument to the addition operation
v0 = torch.randn(3, 8, 64, 64)
m  = Model()
__output__  = m(x1=v0)

