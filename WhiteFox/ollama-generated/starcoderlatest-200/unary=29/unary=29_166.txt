
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=2)
        self.max_val = max_value
        self.min_val = min_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=self.min_val)
        v3 = torch.clamp_max(v2, max_value=self.max_val)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
