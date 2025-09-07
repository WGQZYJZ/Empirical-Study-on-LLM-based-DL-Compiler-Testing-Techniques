
class Model(torch.nn.Module):
    def __init__(self, n1: int = 256) -> None
        self.layer = torch.nn.Linear(n1, 10)

    def forward(self, x):
      v3 = self.layer(x).relu()
      return v3

m = Model()

