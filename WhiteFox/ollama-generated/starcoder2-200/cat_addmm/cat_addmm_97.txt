
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1  = torch.addmm(x1, mat1, mat2)
        t2  = torch.cat([t1], 3)
        return t2
 
# Initializing the model
m = Model()
 
# Inputs to the model
input  = torch.randn(16, 9075834, 9075834) # 3d input tensor for this model example
mat1   = torch.randn(256*256, 9075834)    # 2d matrix to be used in the matrix multiplication operation of this model example
mat2   = torch.randn(9075834, 9075834)    # 2d matrix to be used in the matrix multiplication operation of this model example
__output__  = m(input, mat1, mat2)

