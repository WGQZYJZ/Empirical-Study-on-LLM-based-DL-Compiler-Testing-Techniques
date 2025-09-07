
class Model(torch.nn.Module):
    def __init__(self, inSize1: int=32) -> None:
        super().__init__()

        self.linear = torch.nn.Linear(inSize1 * 4, out_features=8)

    def forward(self, inputA: torch.Tensor, inputB: torch.Tensor): # pragma: no cover
        