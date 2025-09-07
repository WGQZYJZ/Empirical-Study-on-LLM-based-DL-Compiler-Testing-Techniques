
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 2, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 3.0)
        v4 = torch.pow(v3, 1.0 / 3.0)
        v5 = v4 * 0.044715
        v6 = v2 + v5
        v7 = v7 + 1
        v8 = v6 * 0.7978845608028654
        v9 = torch.tanh(v8)
        return v9


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
