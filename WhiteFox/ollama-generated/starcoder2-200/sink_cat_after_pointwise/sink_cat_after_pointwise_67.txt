
class Model(torch.nn.Module):
    def __init__(self, n: int = 42) -> None:
        super().__init__()
        self._n = n

    def forward(self, x1, y1):
        self.