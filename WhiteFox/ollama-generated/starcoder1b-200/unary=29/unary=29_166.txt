
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-6, max_value=2e-6):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


# Initializing the model
m  = Model(max_value=0.5)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
