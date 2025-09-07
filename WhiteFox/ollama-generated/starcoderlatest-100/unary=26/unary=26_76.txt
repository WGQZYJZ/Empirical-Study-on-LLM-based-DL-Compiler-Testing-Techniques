
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 5, stride=2)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        mask = v1 > 0
        negative_slope = -v1 * 0.01
        v2 = torch.where(mask, v1, negative_slope)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 32, 64)
