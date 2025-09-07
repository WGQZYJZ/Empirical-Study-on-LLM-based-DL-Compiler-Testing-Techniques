
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(8, 3, 1)
        self.conv_transpose  = torch.nn.ConvTranspose2d(3, 16, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = torch.clamp(v3, min=0, max=5)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6


# Initializing the model
m = Model()


