
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 32, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.cat([v1], dim=-1)
        v3 = self.conv2(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
