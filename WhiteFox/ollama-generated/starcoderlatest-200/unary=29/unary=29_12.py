
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=4, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=None, max_value=None)
        v3 = torch.clamp_max(v2, min_value=None, max_value=None)
        return v3


# Initializing the model
m = Model()
# Minimum and maximum values of clamp operations provided as keyword arguments
min_value, max_value = None, None

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
