
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v2 * v2 * v2
        v4  = torch.div(v3, 0.044715) + v4
        v6  = v1  + t4 
        v8  = v6 * .7978845608028654  
        v9  = torch.tanh(v8 )
        return v9


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 16, 16)
__output__  = m(x1)