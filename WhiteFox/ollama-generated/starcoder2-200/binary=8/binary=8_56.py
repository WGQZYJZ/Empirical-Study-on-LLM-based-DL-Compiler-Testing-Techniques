
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.other 
        return v2


# Initializing the model
m = Model(torch.zeros(4))


# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
__output__  = m(x1).shape # The output shape of the forward pass should be (16, 8, 62, 62), since the previous conv layer had a stride size of 2.
