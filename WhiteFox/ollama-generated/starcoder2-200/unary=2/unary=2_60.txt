
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 + (v1 ** 3) * 0.044715
        v4 = torch.tanh((v3 * 0.7978845608028654)) + 1 
        v5 = v2 * v4
        return v5

# Initializing the model with inputs to it (different from the previous one)
x1 = torch.randn(1, 3, 64, 64)
m(x1)

