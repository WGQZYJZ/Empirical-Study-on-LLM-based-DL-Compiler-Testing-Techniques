
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v0 = x1
        v1 = self.convtranspose(v0)
        v2 = torch.clamp_min(v1, -5.7690547e+30)
        v3 = torch.clamp_max(v2, 5.8727878e-31)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
