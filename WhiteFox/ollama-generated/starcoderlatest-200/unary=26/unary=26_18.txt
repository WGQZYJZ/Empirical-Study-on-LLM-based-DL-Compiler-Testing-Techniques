
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 16, stride=8, padding=4)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 > 0).float()
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
