
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.activation = torch.nn.Sigmoid()
 
    def forward(self, x):
        v1  = self.convT(x)
        v2  = self.activation(v1) 
        v3  = v1 * v2
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(1, 3, 64, 64)
__output__  = m(x)


