
class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor = torch.ones((8, 3)),
                 mat2: torch.Tensor = torch.ones((7, 6))) -> None:
        super().__init__()

    def forward(self, input_tensor) -> Tuple[torch.Tensor]:
        v1  =  torch.addmm(input=input_tensor,
                           mat1=mat1,
                           mat2=mat2)
        v2  = torch.cat([v1], dim=0)
        return (v2,)


# Initializing the model