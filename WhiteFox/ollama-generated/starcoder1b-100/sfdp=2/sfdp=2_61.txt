
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1) * 0.5
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2) + 1
        v4 = v3 * v2
        v5 = self.conv2(v4) * (v4 > 0.5).float()
        v6 = v5 * (v4 >= 0.5)
        return v6


# Initializing the model
m = Model()


