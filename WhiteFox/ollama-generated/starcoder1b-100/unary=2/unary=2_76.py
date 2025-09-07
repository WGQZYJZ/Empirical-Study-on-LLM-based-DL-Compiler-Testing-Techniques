
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 4, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) * 0.5
        v2 = v1  + 1
        v3 = v1 * v1 * v1 * 0.044715
        v4 = v3 * 0.7978845608028654
        v5 = torch.tanh(v4)
        return v5


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
