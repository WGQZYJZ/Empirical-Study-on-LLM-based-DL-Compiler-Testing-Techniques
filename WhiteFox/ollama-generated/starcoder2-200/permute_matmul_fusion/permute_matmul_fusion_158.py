
class Model(torch.nn.Module):
    def __init__(self, batch: int = 2):
        super().__init__()

        self.linearA1 = torch.nn.Linear(256, 10)

    def forward(self, x1, x2=None):
      v1 = torch.nn.functional.sigmoid(x1.permute([0, 3, 2, 1]))
      v4 = self.linearA1(v1).permute(0, 2, 1)

      if len(v1.shape) > 4 or x2 is None:
        return v4
      else:
        v5 = torch.nn.functional.sigmoid(x1.permute([0,3, 2]))
        return self._bmm_with_linear_a2(v4, v5)

    def _bmm_with_linear_a2(self, A, B):
      r