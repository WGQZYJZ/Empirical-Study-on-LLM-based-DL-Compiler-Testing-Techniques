
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1: torch.Tensor = None) -> torch.Tensor:
        v0  = torch.mm(inp1, inp2) 
        return v0 + inp


# Initializing the model