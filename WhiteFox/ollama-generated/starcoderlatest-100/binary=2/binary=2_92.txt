
class Model(torch.nn.Module):
    def __init__(self, conv=torch.nn.Conv2d):
        super().__init__()
        self.conv = conv(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other # Subtract 'other' from the output of the convolution
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
v2 = m(x1, other=torch.zeros_like(x1)) # Subtract 'other' from the output of the convolution
