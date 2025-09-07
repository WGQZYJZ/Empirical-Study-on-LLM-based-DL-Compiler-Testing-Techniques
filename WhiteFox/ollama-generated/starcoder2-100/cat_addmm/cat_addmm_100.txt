
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2)
        v2 = torch.cat([v1], 0) 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 5) # A 2D tensor of size 4 x 5
mat1  = torch.randn(3, 3) # A 3D tensor of size 3 x 3 x 3
mat2  = torch.randn(3, 3) # A 3D tensor of size 3 x 3 x 3


# Initializing the model
m_init  = Model()
__output1__   = m_init(x1, mat1).shape[0] == __expected__ 
__output2__   = m_init(mat1, mat2).shape[-1] == __expected__ 
