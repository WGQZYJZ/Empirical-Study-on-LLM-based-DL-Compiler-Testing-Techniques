
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = torch.clamp_min(v1, min_value = -3)
        v3 = torch.clamp_max(v2, max_value = 3)
        v4 = self.linear(v3) 
        return v4
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
