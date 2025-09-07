
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 2, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 2
        v4 = torch.cat((v3, v3), dim=-1)
        v5 = v4 * 0.044715
        v6 = v5 + v5
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        return v9


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 16, 16)
