
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * clamp(min=-457900928, max=6.02e-03*5, v1 + 3)
        v3 = v2 / 6
        return v3

# Initializing the model
m = Model()

