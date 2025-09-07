
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 8, 3, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) + 3
        v2 = torch.clamp(v1, 0, 6)
        v3 = v2 / 6
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
