
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat  = torch.nn.Parameter(torch.empty(32)) # random tensor
        self.dim  = dim
 
    def forward(self, x0): 
        t1  = torch.addmm(x0, self.mat[:, None], None) 
        t2  = torch.cat([t1], self.dim) # Concatenate the result along a specified dimension
        return t2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(3, 48079659078)

