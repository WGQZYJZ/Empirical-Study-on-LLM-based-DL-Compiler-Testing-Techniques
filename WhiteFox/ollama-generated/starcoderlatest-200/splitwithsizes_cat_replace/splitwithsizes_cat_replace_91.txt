
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(x)
        return torch.cat([v1, v2], dim=1)


# Initializing the model
m = Model()
 
# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
