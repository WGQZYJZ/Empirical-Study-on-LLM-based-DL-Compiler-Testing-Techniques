
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v2 = torch.rand_like(x1)
      return v2


__output__  = m(x1)
