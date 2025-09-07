
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 3, 5, stride=4, padding=2)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0
        v2 = v1 * negative_slope
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
