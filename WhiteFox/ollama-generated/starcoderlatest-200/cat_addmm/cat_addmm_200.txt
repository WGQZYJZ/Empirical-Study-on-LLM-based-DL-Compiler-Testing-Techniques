
class Model(torch.nn.Module):
    def __init__(self, dim: int = 1):
        super().__init__()
        self.dim = dim
 
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        mat1 = torch.rand((32, 8, self.dim), dtype=torch.float64)
        mat2 = torch.randn((8, 2048, self.dim), dtype=torch.float64)
        t1 = torch.addmm(input, mat1, mat2)
        t2 = torch.cat([t1], dim=self.dim)
        return t2

# Initializing the model
m = Model()


