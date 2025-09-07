
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-32, max_value=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        min_v1 = x1.min().detach()
        max_v1 = x1.max().detach()
        t1  = torch.clamp_min(v1, min_value=min_v1).clamp_max(max_value=max_value)
        v2  = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3) + 1
        v5 = v2 * v4
        return v5


# Initializing the model
m = Model()

