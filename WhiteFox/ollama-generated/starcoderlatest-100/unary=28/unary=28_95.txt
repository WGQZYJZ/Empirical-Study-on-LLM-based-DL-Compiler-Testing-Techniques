
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=255.):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64, 256)
        self.softmax = torch.nn.Softmax()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
 
        return self.softmax(self.linear(v3))
# Initializing the model with keyword arguments as input for clamping
m = Model(min_value=0., max_value=255.)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
