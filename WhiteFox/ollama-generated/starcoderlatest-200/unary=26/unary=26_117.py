
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=16)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0
        negative_slope = 0.2
        v2 = v1 * negative_slope
        return v2
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
