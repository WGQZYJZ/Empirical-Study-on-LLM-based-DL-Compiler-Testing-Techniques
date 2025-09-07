
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1)

    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0) # Clamped minimum at 0
        v4  = torch.clamp(v3, max=6) # Clamped maximum at 6
        v5  = v4 / 6
        return v5


# Initializing the model
m = Model()
x1  = torch.randn(1, 8, 27, 27)
__output__  = m(x1)

