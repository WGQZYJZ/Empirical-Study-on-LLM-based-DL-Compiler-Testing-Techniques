
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1: torch.Tensor, t2: torch.Tensor) -> torch.Tensor:
        v1  = torch.cat([t1, t2], dim=3)
        v2  = v1.view(-1, ...)
        v3  = torch.relu(v2)
        return v3


# Initializing the model