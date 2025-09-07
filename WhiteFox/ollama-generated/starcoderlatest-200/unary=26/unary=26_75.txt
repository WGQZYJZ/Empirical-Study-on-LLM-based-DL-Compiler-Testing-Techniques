
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=2)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        t1 > 0
        v2 = v1 * negative_slope
        return torch.where(t1 > 0, v1, v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
