
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other  = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other # Subtract 'other' from the output of the convolution (tensor or scalar).
        return v2

# Initializing the model
m = Model(torch.randn((3, 8, 64, 64)))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # The shape of 'other' is determined by user's input.
__output__  = m(x1)