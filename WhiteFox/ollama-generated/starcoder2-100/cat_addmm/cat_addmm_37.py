
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()

        mat1 = torch.randn((8052673), 4)
        mat2 = torch.randn((4, 69))

    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2) # perform a matrix multiplication of mat1 and mat2 and add it to the input

        return torch.cat([v1], dim)

# Initializing the model
m  = Model(0).cuda()

# Inputs to the model
x1  = torch.randn(3, 69).cuda()
__output__  = m(x1)

