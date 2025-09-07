
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -6.) # Applying clamp function
        v3  = torch.clamp_max(v2, 48.) # Applying clamp max function
        return v3


# Initializing the model