

class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.convT(x1)
        mask = v1 > 0
        v2 = negative_slope * v1
        v4 = v1.masked_fill_(mask, v2)
 
        return v3

m = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)

__output__= m(x1)

