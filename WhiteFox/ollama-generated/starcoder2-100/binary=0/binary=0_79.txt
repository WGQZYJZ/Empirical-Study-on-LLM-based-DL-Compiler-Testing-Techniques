
class Model(torch.nn.Module):
    def __init__(self, o):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + o
        return v2


# Initializing the model with an additional parameter `o` as keyword argument to add function.
m  = Model(torch.randn(8,3,64,64))

# Inputs to the model:
x1 = torch.randn(1, 3, 64, 64)

