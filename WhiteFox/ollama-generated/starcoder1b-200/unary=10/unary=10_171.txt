
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(torch.add(v1, 3), 0)
        v3 = torch.clamp_max(v2, 6) / 6
        v4 = torch.mul(v3, 6) + 1
        return v4


# Initializing the model
m = Model()

