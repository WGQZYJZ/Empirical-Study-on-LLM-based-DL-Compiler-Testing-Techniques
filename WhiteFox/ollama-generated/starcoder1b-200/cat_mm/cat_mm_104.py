
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x2 = self.conv1(x1)
        return self.conv2(torch.cat([x2, x2], dim=0))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4, 64, 64)
