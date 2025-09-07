
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.leaky_relu(F.pad(self.conv(x1), (0, 0, 0, 0, 0, 1, 1)), inplace=True)
        v2 = F.tanh(v1) * 0.5
        v3 = (v1 ** 2) * v2
        v4 = F.leaky_relu(v3, inplace=True)
        v5 = v6 = v4 * 0.044715
        v8 = (x1 + v6) * 0.7978845608028654
        return F.leaky_relu(v8, inplace=True)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
