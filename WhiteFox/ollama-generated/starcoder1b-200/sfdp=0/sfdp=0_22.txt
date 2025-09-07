
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1  = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.bn2  = torch.nn.BatchNorm2d(8)
 
    def forward(self, x1):
        v1 = self.bn1(self.conv1(x1))
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = self.bn2(self.conv2(v2))
        v7 = v6 * v5
        return v7


# Initializing the model
m = Model()


