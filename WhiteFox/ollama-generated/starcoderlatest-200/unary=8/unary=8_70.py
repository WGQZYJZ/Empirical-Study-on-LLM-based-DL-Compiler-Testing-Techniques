
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) + 3
        v2 = torch.clamp(v1, min=0, max=6)
        v3 = v1 * v2
        v4 = v3 / 6
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 512, 512)
