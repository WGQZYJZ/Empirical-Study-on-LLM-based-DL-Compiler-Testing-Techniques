
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2) 
        return torch.cat([v1], dim=0)


# Initializing the model
m = Model()
mat1 = torch.rand(32*64**2).reshape(-1, 32, 64, 64).float().to('cuda')
mat2 = torch.rand(64**2).reshape(32, -1, 1).float().to('cuda')


# Inputs to the model
x1 = torch.rand(32*64**2).reshape(-1, 32, 64, 64)


 __output__  = m(x1, mat1, mat2)

The input tensor is of size [25000] and the output of the model will also be of size [25000].

# Evaluation
