
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v0 = self.deconv(x1)
        v1 = torch.sigmoid(v0)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
__output__  = m(x1)

