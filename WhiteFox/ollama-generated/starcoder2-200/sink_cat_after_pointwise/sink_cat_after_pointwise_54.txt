
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1: torch.Tensor) -> torch.Tensor:  # Type annotations are not required for this task!
        