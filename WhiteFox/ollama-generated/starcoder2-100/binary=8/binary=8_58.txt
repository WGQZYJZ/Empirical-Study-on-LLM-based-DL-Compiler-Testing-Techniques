
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other
        return v1


# Initializing the model with a dummy keyword argument tensor.
m = Model(other=torch.randn(4))

# Inputs to the model
x1  = torch.randn(3, 8, 20, 56)

__output__  = m(x1)
