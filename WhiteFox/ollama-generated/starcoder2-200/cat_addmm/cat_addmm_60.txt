
class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor, mat2: torch.Tensor, dim: int = 0) -> None:
        super().__init__()
        self._mat1 = mat1
        self._mat2 = mat2
        self._dim = dim
 
    def forward(self, input):
        v1 = torch.addmm(input, self._mat1, self._mat2) 
        return torch.cat([v1], self._dim)


# Initializing the model with some initial values for the matrices:
mat1  = torch.ones(3, 5) * 0.7
mat2  = torch.ones(64*64, 5) * 0.8
m  = Model(mat1=mat1, mat2=mat2, dim=0)

 # Inputs to the model
x1  = torch.randn(32, 64*64)
__output__  = m(x1)

