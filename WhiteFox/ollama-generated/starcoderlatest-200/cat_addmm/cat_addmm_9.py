
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        mat1 = torch.ones([3, 8])
        mat2 = torch.ones([3, 4])
        t1 = torch.addmm(x1, mat1, mat2) 
        dim=0
        t2 = torch.cat([t1], dim)
        return t2

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
