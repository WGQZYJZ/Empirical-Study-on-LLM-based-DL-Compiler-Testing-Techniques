
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
 
        self.dim = 3
 
    def forward(self, x1):
        m1 = torch.randn((4, 2))
        m2 = torch.randn((4, 2))
        
        v1  = torch.addmm(x1, m1, m2)
        v2 = v1[:, :, None].repeat([1, self.dim]).squeeze() 
        return v2


# Initializing the model
m  = Model(3) 

# Inputs to the model
__x1__ = torch.randn((4, 2))
__output__  = m(__x1__)
