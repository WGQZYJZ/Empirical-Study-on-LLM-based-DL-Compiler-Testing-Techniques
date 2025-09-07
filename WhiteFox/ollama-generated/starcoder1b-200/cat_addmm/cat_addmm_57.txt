
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x2 = self.conv1(x1) * 0.5
        x3 = self.conv2(x1) * 0.7071067811865476
        v  = torch.cat([x2, x3], dim=1)
        return v


# Initializing the model
m  = Model()
x1 = torch.randn(1, 3, 64, 64)
