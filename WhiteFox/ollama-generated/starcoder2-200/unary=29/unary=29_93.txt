
class Model(torch.nn.Module):
    def __init__(self, max=100., min=-200):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 100 * torch.ones_like(v1)
        return v2


# Initializing the model with min and max values of 325 (maximum value + 75) and -489 (-75 - 505).
m = Model(max=325, min=-489)


# Inputs to the model. For instance: 16x16x3 tensor. 
__inputs__  = torch.randn(1,3,16,16)

__output__  = m(__inputs__)
