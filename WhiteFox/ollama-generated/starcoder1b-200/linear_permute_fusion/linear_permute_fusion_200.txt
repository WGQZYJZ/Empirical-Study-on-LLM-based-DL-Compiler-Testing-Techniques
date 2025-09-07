
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self._call_linear(x1)
        return v1

    def _call_linear(self, x2):
        