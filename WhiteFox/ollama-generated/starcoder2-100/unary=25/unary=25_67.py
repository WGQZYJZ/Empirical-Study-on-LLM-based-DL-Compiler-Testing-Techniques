
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1) # linear transformation 
        v2  = v1 > 0 # boolean mask
        negative_slope   = 0.35

        v3 = v1 * negative_slope # element-wise multiplication by the negative slope
        
        v4 = torch.where(v2, v1, v3) 
        
        return v4


# Initializing the model: 
m=Model()


# Inputs to the model
x1   =torch.randn(8,)
__output__    = m(x1)

