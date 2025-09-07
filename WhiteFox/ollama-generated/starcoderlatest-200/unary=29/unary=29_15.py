
class Model(torch.nn.Module):
    def __init__(self, kernel_size=5, stride=2, padding=3, min_value=-1.0, max_value=1.0):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, (kernel_size, kernel_size), (stride, stride), (padding, padding))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
