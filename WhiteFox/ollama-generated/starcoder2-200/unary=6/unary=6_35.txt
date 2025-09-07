
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6) 
        v5 = v1 * v4
        v6 = v5 / 6 # Divide the output of the multiplication by 6
        return v6

# Initializing the model with different parameters to ensure different outputs at each run
m1 = Model()
x1 = torch.randn(1,3,28,28)

__output___  = m1(x1)

