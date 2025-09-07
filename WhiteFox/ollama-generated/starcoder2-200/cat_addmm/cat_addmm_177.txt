
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, m1, m2):
        v1  = torch.addmm(x1, m1, m2) 
        v2  = torch.cat([v1], self.dim) 
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1=torch.randn(4,50)
mat1 = torch.randn(3,50)
mat2 = torch.randn(3,39708)
__output__  = m(x1, mat1, mat2)

# Model 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, m1):
        v1  = torch.addmm(x1, m1) 
        return v1

 # Initializing the model
m  = Model()
 # Inputs to the model
x1=torch.randn(400,50)
mat2 = torch.randn(39708,39708)
__output__  = m(x1, mat2)

