
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v2, 3.0)
        v4 = torch.cat([torch.pow(v3, 2.7), torch.pow(v3, 3.0)], dim=-1)
        v5 = v1 + v4
        v6 = torch.tanh(v5)
        v7 = v2 * v6
        return v7


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 16, 16)
