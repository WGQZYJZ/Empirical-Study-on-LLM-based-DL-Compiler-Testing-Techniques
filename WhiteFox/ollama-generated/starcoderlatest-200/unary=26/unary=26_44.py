
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 4, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        # Apply the Leaky ReLU function following a transposed convolution
        return F.leaky_relu(v1, negative_slope)

# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
