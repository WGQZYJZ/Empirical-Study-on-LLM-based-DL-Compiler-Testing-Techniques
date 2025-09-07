
class Model(torch.nn.Module):
    def __init__(self, min_value=-1.0, max_value=1.0):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
        self.clamp_min = torch.nn.ClampMin(-1)
        self.clamp_max = torch.nn.ClampMax(1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model with specified minimum and maximum values
m = Model(min_value=-20.0, max_value=80.0)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
