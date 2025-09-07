
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        clamped_v2 = torch.clamp_min(v1, self.min_value)
        clamped_v3 = torch.clamp_max(clamped_v2, self.max_value)
        return clamped_v3

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 8, 40, 40)
