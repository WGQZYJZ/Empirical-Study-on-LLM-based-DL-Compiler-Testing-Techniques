
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0, max=6)
        v4  = v3 * v1 
        v5  = v4 / 6
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 8, 8) # x1 is a random tensor of shape (batch size 1, channel 3, width 8, height 8).
__output__  = m(x1)

