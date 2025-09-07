
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * -0.7071067811865476  # Negative slope of the Leaky ReLU
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
