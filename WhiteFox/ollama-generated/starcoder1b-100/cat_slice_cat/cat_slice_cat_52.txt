
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 5, stride=2, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = self.conv2(torch.cat([v1, v5], dim=1))
        return v6


# Initializing the model
m = Model()

