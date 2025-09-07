
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other
        return v2


class Other(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x2):
        v2 = 2 * x2 # Multiply the tensor by two 
        return v2


# Initializing the model
m1 = Model(Other())

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
v1 = m1(x1)
