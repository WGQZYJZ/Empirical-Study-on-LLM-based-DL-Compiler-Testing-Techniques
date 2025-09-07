
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1) + 3 
        v2 = torch.clamp_min(v1, 0) # clamp minimum 0 and maximum 6
        v4 = v2 / 6.0
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 8, 5, 5)
