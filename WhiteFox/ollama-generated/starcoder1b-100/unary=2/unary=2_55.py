
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 ** (v1 * 0.044715)
        v4 = v3 * 0.7978845608028654
        v5 = torch.tanh(v4 + 1)
        v6 = v2 * v5
        return v6


# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
