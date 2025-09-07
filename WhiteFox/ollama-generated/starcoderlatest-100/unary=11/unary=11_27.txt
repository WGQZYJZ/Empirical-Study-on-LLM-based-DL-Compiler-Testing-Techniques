
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transp = torch.nn.ConvTranspose2d(3, 8, 4, stride=4)
 
    def forward(self, x1):
        v1 = self.conv_transp(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0.0)
        v4 = torch.clamp(v3, max=6.0)
        v5 = v4 / 6
        return v5

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
