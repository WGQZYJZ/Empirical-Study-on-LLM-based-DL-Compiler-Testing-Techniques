
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(8,3,1)
    
    def forward(self,x):
            v1 = self.convT(x)
            v2 = torch.sigmoid(v1)
            return v2


m = Model()
x = torch.randn(10, 5,64,64)

__output__= m(x)