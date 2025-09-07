
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = v1 + 3 
        v3  = torch.clamp(v2, min=0)  
        v4  = torch.clamp(v3, max=6) 
        v5  = v1 * v4
        v6  = v5 / 6
        return v6


# Initializing the model
m = Model()
# Inputs to the model
x2 = torch.randn(1,8, 64, 64) 

# Calling the model with inputs x1 and x2
__output__1 = m(x1) # This line is used for the system to evaluate the first call to the model
__output__2 = m(x2)

