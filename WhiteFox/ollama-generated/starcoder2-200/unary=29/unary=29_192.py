
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = v1.clamp_min(-90.6478535)
        v3 = v2.clamp_max(90.6478535) # clamp_max(v2, 90.6478535) also possible
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)