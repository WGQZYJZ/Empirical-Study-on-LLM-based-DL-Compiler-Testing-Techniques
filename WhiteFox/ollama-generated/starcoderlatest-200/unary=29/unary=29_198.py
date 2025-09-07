
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv_transposed = torch.nn.ConvTranspose2d(8, 3, 2, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transposed(x1)
        v2 = torch.clamp(v1, min_value=min_value, max_value=max_value)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
