
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transposed = torch.nn.ConvTranspose2d(3, 8, kernel_size=16, stride=16)
 
    def forward(self, x1):
        v1 = self.conv_transposed(x1) > 0
        negative_slope = torch.zeros(v1.shape).float() - 0.2
        v3 = v1 * negative_slope
        result = torch.where(v1, x1, v3)
        return result


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
