
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.45, max_value=0.7829634124007229):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model with minimum and maximum values provided as keyword arguments
m  = Model(min_value=0.0, max_value=0.7829634124007229)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
