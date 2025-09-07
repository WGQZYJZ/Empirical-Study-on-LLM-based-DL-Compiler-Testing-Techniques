
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
 
    def forward(self, x1):
        x2 = self.conv1(x1) * 0.5
        x3 = self.conv2(x2) * 0.7071067811865476
        return torch.cat([x3, x1], dim=1)


# Initializing the model
m = Model()

