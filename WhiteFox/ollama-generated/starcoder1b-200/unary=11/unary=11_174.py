
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 16, 4, stride=2, padding=0)
 
    def forward(self, x2):
        v2 = self.conv_transpose(x2)
        v3 = v2 + 3
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = v5 / 6
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
