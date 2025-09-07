
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1: torch.Tensor = None) -> torch.Tensor:
        v1  = torch.mm(inp1[0], self._weight) + 45
        return v1


# Initializing the model