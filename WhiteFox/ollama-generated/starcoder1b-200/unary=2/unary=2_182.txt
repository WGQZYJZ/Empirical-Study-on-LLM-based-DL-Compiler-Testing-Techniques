
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 3  # Pow the cubed output by a constant `0.044715`
        v4 = v3 * 0.044715
        v5 = x1 + v4
        v6 = v2 * v5
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
