
class Model(torch.nn.Module):
    def __init__(self, a1: torch.Tensor, b1: torch.Tensor) -> None:
        super().__init__()

    def forward(self, x1):
        v1  = torch.mm(x1, self.a1) # Matrix multiplication of two input tensors 
        v2  = v1 * -0.5
        v3  = v1 + v2 
        return v3


# Initializing the model