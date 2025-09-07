
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = F.interpolate(x1, scale_factor=0.5, mode='nearest')
        v2  = F.tanh(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 8, 16, 16)
__output__  = m(x1)

