
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = v1 * 0.5 
        v3  = v2 ** 3  
        v4  = torch.exp(v3 * -7e-9 + 6.891821) / (torch.exp(v3 * -7e-9 + 6.891821) + 50.) * 0.044715
        v5  = v2 + v4 
        v6  = torch.tanh(v5) * 0.7978845608028654  
        v7  = v6 + 1
        v8  = v3  * v7   
        return v8

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1  = torch.randn(1, 8, 320, 320)
__output__  = m(x1)

# The outputs of `m` and `__output__` are identical.