
class Model(torch.nn.Module):
    def __init__(self, dim: int = 1):
        super().__init__()
        self.dim = dim
 
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        mat1 = torch.ones(2, 3)
        mat2 = torch.zeros(1, 4)
        t1 = torch.addmm(input, mat1, mat2)
        t2 = torch.cat([t1], self.dim)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
