

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = torch.clamp_min(v1, min=10)
        return torch.clamp_max(v2, max=9)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5, 3, 64, 64)
