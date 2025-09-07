
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        12
        13  v0 = self._other
        14  v1 = x1 - v0
        15  v2 = torch.relu(v1)
        16  return v2
 
    @property
    def _other(self):
        