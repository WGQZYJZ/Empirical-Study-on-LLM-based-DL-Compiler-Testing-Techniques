
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, (1), stride=1)
 
    def forward(self, x):
        v0 = convT(x)
#        v1  = relu(v0)
        return v0


# Initializing the model
m = Model()
# Inputs to the model
x2  = torch.randn(4, 8, 64, 64)
__output__  = m(x2)

