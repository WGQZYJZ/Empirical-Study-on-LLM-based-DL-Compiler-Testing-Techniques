
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1   = self.conv(x1) 
        v2   = v1 * 0.5
        v3   = v2**2
        v4   = v3 * v1
        v5   = (v4*0.7978845608028654) + 0.044715
        v6   = v1+v5 
        v7   = torch.tanh(v6)*(-torch.exp(v3))
        v8   = (-torch.exp(v3))/((-torch.exp(v2))+1)
        v9   = 0.7978845608028654 * v8 + ((-torch.exp(v1))*((torch.exp(v3))**(-1)))
        v10  = torch.tanh(v1+v9)
        return v10


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
