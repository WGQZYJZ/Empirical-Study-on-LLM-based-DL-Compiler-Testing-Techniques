
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x2):
        v5  = self.conv_transpose(x2) / 6
        v4  = torch.clamp(v5 + 3, min=0)
        v3  = torch.clamp(v4, max=6)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
