
class Model(torch.nn.Module):
    def __init__(self, max_value=0.9, min_value=-1.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

# Initializing the model with keyword arguments
m  = Model(min_value=-0.78, max_value=0.52)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
