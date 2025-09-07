
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 1e-2):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=2, stride=2)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        return torch.where(v2, v1, v3)


# Initializing the model
m = Model()


