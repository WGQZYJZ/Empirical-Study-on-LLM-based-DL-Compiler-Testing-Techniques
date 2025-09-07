
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        return self.conv(x1) + self._relu(x1)
 
    def _relu(self, x):
        return torch.relu(x)

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
