
class Model(torch.nn.Module):
    def __init__(self, dim1: int = 5, dim2: int = 8) -> None:
        super().__init__()
        self.mat1 = torch.randn(dim1 * dim2, 3).to("cpu")
        self.mat2 = torch.randn(dim1 + 64, 99).to("cuda")
 
    def forward(self, x):
        v1  = torch.addmm(x, mat1)
        return torch.cat([v1], dim=0)


# Initializing the model
m  = Model()
 
# Inputs to the model
x  = torch.randn(4, 3) + 8 # Input tensor with shape (N, D) = (4, 3), where N is 4 and D is 3
__output__  = m(x)

