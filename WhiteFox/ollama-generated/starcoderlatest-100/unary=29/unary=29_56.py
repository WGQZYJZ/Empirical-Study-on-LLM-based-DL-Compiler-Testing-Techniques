
class Model(torch.nn.Module):
    def __init__(self, min_value=-5.0, max_value=20.0):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(1, 3, kernel_size=4, stride=8, padding=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
