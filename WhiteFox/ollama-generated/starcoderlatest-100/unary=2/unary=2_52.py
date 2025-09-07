
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(16, 32, 4, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = v1 * 0.5
        v3 = v1 * (v1 * v1) * 0.044715
        v4 = v3 + v1
        v5 = v4 * 0.7978845608028654
        v6 = torch.tanh(v5)
        v7 = v6 + 1
        v8 = v2 * v7
        return v8


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 4, 4)
