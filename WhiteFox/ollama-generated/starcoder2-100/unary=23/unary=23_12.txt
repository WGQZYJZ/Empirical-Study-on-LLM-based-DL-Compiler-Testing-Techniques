
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.deconv(x)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(4800,3,64,64)
__output__  = m(x)
