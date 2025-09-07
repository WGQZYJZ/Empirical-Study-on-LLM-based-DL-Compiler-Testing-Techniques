
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convTrans(x1)
        v2  = torch.tanh(v1)
        return v2

m  = Model()

 # Inputs to the model
 
x1 = torch.randn(10, 3, 64, 64)
__output__  = m(x1)
