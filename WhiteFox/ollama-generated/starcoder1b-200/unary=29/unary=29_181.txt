
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv_transpose(x)
        return torch.clamp_min(v, min_value)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 8, 32, 64)
