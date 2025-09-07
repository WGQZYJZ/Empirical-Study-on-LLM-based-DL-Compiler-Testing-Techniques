
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1 = deconv(x1)
        v2 = torch.clamp_min(v1, min=0)
        return torch.clamp_max(v2, max=4)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 8, 50, 67)
__output__  = m(x1)

