
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1  = self.conv(x1)
        v2  = torch.erf(v1 * 0.5 + x2 * 0.7071067811865476) + 1
        v3  = v2 * 0.23890593276193937
        v4 = self.conv(v3)
        v5 = v2  * v4
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
