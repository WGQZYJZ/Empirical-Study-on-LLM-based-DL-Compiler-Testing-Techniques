
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1: torch.Tensor, t2: torch.Tensor) -> torch.Tensor:  # pylint: disable=unused-argument
        v = torch.cat([t1, t2], dim=-1).view(-1, 256, 8, 4).relu()
        return v

# Initializing the model
m = Model()

