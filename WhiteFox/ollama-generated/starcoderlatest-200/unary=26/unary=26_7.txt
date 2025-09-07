
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        t1 = self.conv_transpose(x1) > 0
        negative_slope = -0.02
        t3 = t1 * negative_slope
        t4 = torch.where(t2, t1, t3)
        return t4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
