
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()

    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2)
        v2 =  torch.cat([v1], 0)
        return v2


# Initializing the model
mat1  = torch.randn(3, 4).double()
mat2  = torch.randn(3, 5).double()
m  = Model(mat1, mat2)

 # Inputs to the model
x1  = torch.rand(90000000, 4).double().cuda()
