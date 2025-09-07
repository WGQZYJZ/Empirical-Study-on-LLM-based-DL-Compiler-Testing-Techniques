
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, kernelSize=1, stride=1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 + 3 
        v3  = torch.clamp(v2, min=0, max=6 ) # clamp(v3, 0, 5)
        v4  = v3 / 6
        return v4


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8, 3, 29, 29) # [batchSize, channels, height, width]
__output__  = m(x1)

