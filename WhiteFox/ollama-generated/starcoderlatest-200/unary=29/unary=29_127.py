
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value=10):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 5, stride=4, padding=2)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=self.min_value)
        v3 = torch.clamp_max(v2, max_value=self.max_value)
        return v3
# Initializing the model
m = Model(0.5, 10)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
