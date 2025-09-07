
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v0 = torch.sigmoid(self.deconv(x1))
        return v0


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)