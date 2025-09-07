
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp(v1, min_value, max_value)
        return v2


# Initializing the model
m = Model(min_value=0., max_value=1.)


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
