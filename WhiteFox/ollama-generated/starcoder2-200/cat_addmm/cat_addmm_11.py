
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
 
    def forward(self, x1):
       v1 = torch.addmm(x1, mat1, mat2)
       v2 = torch.cat([v1], dim) 
       return v2


# Initializing the model 
m  = Model()
mat1  = torch.randn((504739, 6))
mat2  = torch.randn(582544, 1)
 
# Inputs to the model
x1  = torch.randn(310548, 2)
 
