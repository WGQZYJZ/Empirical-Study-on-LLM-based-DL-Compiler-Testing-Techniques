
class Model(torch.nn.Module):
    def __init__(self, min_value: float = 0.0, max_value: float = 1.0):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.clamp(v1, min=-0.45946373, max=0.45946373)
        v3 = torch.clamp(v2, min=min_value, max=max_value)
        return v3


# Initializing the model and provide the minimum and maximum values as arguments to it
m = Model(min_value=-0.45946373, max_value=0.45946373)
