
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, inp: torch.Tensor) -> torch.Tensor: 
        v2 = (
            torch.mm(x1, inp) +
            self._constant_fn(0).view(-1,)  # this is a constant tensor
        )
        return v2

# Initializing the model
m = Model()

