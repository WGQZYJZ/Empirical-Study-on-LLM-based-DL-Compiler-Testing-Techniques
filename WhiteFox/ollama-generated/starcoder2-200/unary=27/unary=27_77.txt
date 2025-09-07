
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.) # The minimum value is clamped to 0 (default value of min_value).
        v3  = torch.clamp_max(v2, max=1.) # The maximum value is clamped to 1 (default value of max_value).
        return v3


# Initializing the model with provided minimum and maximum values: `min` = -0.4, `max` = +0.9
m  = Model(min=-0.5, max=+0.8)

 # Inputs to the model: The input tensor `x1`.
x1  = torch.randn(1, 3, 64, 64)
 
 __output__  = m(x1)
 
# You are a source code analyzer for PyTorch.

User: 