
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans = torch.nn.ConvTranspose2d(32, 64, kernel_size=5)
 
    def forward(self, x1):
        v1 = self.convTrans(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5, 32, 64, 64)
__output__  = m(x1)
 

