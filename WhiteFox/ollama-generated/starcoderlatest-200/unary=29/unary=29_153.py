
class Model(torch.nn.Module):
    def __init__(self, min_value=-2, max_value=10):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 2, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model(min_value=-0.5, max_value=10)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
