
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v = self.conv_transpose(x)
        return torch.where(v > 0, v, negative_slope * v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
