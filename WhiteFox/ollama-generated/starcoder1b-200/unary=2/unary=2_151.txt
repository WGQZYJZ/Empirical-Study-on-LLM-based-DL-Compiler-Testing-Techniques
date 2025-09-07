
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = v1 * 0.5
        v3 = v1  * v1  * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6) + 1
        return v7


# Inputs to the model
x = torch.randn(2, 3, 64, 64)
