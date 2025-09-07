
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=-0.5) # Change to clamp(-0.9, -0.4, -0.3)
        v3 = torch.clamp_max(v2, max_value=0.8)  # Change to clamp(0.6, 0.7, 0.1) 
        return v3


# Initializing the model