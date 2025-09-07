
class Model(torch.nn.Module):
    def __init__(self, dim: int = 1) -> None:
        super().__init__()
 
    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        split_tensors = torch.split(x1, [2], dim=dim)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
