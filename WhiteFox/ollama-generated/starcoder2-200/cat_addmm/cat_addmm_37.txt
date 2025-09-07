
class Model(torch.nn.Module):
    def __init__(self, dim=1024):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1[:, :], mat1, mat2) 
        v2  = torch.cat([v1], dim)
        return v2
 
 # Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(1024, 3 * 64 * 64)
 mat1 = torch.zeros((1024,), device=device).float() 
 mat2 = torch.zeros_like(mat1)
 __output__  = m(x1)

