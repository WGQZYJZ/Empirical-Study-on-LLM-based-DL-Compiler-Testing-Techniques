
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1)
        v2  = v1  *  0.5
        v3  = (v2*v2*v2)*0.7978845608028654
        v4  = torch.tanh(v3)+1 
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 1, 1)

__output__  = m(x1)