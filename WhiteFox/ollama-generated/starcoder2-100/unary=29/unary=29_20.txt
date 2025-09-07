
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min(-5)) # Clamps the value of v1 to a minimum value -5.
        v3  = torch.clamp_max(v2, max_(100)) # Clamps the value of previous operation to a maximum value 100.
        return v3


# Initializing the model