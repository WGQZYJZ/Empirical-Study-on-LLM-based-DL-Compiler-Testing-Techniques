
class Model(torch.nn.Module):
    def __init__(self, min=0.25, max=0.849):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=2, padding=1)
 
    def forward(self, x1, min_value = 0.25, max_value = 0.849):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

# Initializing the model
m = Model(min=0.5, max=0.957843)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
