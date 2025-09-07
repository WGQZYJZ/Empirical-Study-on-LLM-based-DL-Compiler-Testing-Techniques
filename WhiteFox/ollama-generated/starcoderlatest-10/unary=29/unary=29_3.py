
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 16, stride=8, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=kwargs['min'], max_value=kwargs['max'])
        v3 = torch.clamp_max(v2, min_value=0.5, max_value=1.0)
        return v3


# Initializing the model
m = Model(min=0.01, max=0.9)

# Inputs to the model
x1 = torch.randn(1, 8, 240, 320)
