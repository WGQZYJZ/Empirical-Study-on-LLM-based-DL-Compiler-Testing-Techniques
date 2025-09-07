
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v0  = x1
        v4  = torch.clamp((v0 + 3), min=0, max=6)
        v5  = self.conv(v4) * v4 / 6

        return v5

m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
 
 