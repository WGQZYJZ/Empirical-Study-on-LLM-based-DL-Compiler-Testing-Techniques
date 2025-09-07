
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(3, 8, kernelSize=1)
 
    def forward(self, x):
        v1 = self.convTranspose(x)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
 
 # Inputs to the model
 x1 = torch.randn(3, 8, 64, 64)
 
__output__  = m(x1)
