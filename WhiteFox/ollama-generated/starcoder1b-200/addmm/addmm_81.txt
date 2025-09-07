
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1: torch.Tensor, inp: torch.Tensor) -> torch.Tensor:
        return torch.mm(x1, inp) + inp  # Apply matrix multiplication to two input tensors


# Initializing the model
m = Model()

