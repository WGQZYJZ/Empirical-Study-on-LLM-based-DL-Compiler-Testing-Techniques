

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self._linear = torch.nn.Linear(32, 10)
        self._activation = torch.nn.SELU()
        
    def forward(self, x):
        v1 = self._linear(x)

        v2 = (v1 + 3).clamp_(min=0, max=6)
        v3 = ((v2 * self._activation(v2)) / 6.).sum(-1)

        return v3
