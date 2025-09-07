
class Model(torch.nn.Module):
    def __init__(self, min_value=-10.0, max_value=10.0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.clamp = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = (torch.clamp_min(v4, self.min_value) + self.max_value).view(-1)
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()
