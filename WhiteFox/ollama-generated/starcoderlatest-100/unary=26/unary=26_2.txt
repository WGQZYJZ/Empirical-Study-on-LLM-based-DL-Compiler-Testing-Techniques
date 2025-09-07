
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 16, kernel_size=2, stride=2)

    def forward(self, x1, negative_slope):
        v1 = self.conv_transpose(x1)
        t1 = v1 > 0
        v2 = v1 * negative_slope
        t3 = torch.where(t1, v2, v1)
        return t3

# Initializing the model
m = Model()
negative_slope = torch.tensor([0], dtype=torch.float).to(x1)

# Inputs to the model
x2  = torch.randn(256, 16, 8, 8)
