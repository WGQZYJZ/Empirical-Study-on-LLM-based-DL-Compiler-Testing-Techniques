
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1) + other
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()
other  = torch.randn(1, 3, 64, 64)
