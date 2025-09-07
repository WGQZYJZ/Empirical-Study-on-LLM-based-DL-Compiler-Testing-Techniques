
class Model(torch.nn.Module):
    def __init__(self, max_value=10, min_value=-5):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=4)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.5) # Min value is set to 0.5
        v3  = torch.clamp_max(v2, max=7.) # Max value is set to 7.
        return v3


# Initializing the model