
class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor, mat2: torch.Tensor, dim=0) -> None:
        super().__init__()
 
    def forward(self, input: torch.Tensor):
        v1  = torch.addmm(input, mat1, mat2)
        return torch.cat([v1], dim)


# Initializing the model