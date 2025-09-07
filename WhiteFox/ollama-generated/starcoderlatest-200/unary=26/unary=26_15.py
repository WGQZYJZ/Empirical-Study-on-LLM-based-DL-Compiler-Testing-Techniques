
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.1):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 16, stride=8, padding=4)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        # Note that when multiplying by the negative slope, t1 is used instead of -t1 in the torch.where call below
        # This allows for using a similar pattern for Leaky ReLU operations preceding convolutions and transposed convolutions
        v2 = torch.where(v1 > 0, x1, -x1 * negative_slope)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
