

class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, dim=0):
        super().__init__()
        self.addmm = torch.addmm
        
    def forward(self, x):
        v1  = self.addmm(x)
        return self.concat(v1, dim)


# Initializing the model
m = Model(mat1, mat2)
__output__  = m(x)

# Input  to the model
x= torch.randn(4096, 3584))


