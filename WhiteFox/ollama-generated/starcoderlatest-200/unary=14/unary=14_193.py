
class GLU(torch.nn.Module):
    def __init__(self, input_dim: int):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(input_dim, input_dim, 1, stride=1, padding=0)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = self.sigmoid(v1)
        v3 = v1 * v2
        return v3

# Initializing the model
m = GLU(8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
