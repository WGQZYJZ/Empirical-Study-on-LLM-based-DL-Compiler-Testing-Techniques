
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x) * 0.5 + self.conv(x) * 0.7071067811865476
        return torch.sigmoid(v)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
