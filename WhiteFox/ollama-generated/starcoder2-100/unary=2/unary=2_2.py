
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1)
        v2  = v1 * 0.5 
        v3  = v1 * (v1 ** 3)  
        v4  = torch.tanh(v3 + .7978845608028654 ) 
        v5  = torch.sin(v3 + .044715)
        v6  = torch.cos(v5 + 0.)
        return v2 * v6


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) 

