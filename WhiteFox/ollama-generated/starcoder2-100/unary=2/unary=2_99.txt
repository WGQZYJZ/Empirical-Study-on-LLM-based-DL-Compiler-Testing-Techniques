
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x):
        v0 = self.convT(x)
        v1 = v0 * 0.5
        v2 = v1  * v1 * v1 
        v3 = v2 + 0.4971855290637859
        v4 = v1 + v3
        v5 = v4 * 0.8198719847498578
        v6 = torch.tanh(v5) 
        v7 = v6 + 1
        v8 = v1* v7
        return v8


# Initializing the model
m  = Model()
# Inputs to the model
x  = torch.randn(1,3,240,240)
 
__output__  = m(x)

