
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
        # Matrix multiplication tensor 1 and input tensor for the model
        self.mat1 = torch.randn((4, 2))
        self.dim = dim
    
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat1)
        
        return torch.cat([v1], self.dim)


# Initializing the model with a given dimension
m = Model(3)

 # Inputs to the model
t = torch.randn((4, 6))
 
