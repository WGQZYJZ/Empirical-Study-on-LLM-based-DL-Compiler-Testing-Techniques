
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.cat([x1, torch.randn(size=(2, 5, 64, 64), dtype=torch.float)], dim=0)
        v2 = self.conv(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(size=(2, 3, 64, 64))
