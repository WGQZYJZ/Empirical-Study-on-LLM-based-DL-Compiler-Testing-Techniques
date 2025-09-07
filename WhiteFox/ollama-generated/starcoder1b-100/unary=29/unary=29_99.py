
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv_transpose(x1, **kwargs)
        v2 = v1 * torch.clamp_min(0.5, kwargs["min"])
        v3 = v1 * torch.clamp_max(v2, kwargs["max"])
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
