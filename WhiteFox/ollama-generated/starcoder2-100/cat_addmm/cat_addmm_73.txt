
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim  = dim
 
    def forward(self, input1, input2):
        t1 = torch.addmm(input1, mat1, mat2) 
        t2 = torch.cat([t1], dim)  
        return t2


# Initializing the model and setting `dim` to zero for the concatenation operation 
m  = Model()
mat1 = torch.randn(64*32*8, 1024).reshape(64 * 32, 8, 1024)
mat2 = torch.zeros(512*9, dtype=torch.float)
x1 = torch.randn(64*32*8)
x2 = torch.randn(64*32*8)
__output__  = m(x1, x2)

