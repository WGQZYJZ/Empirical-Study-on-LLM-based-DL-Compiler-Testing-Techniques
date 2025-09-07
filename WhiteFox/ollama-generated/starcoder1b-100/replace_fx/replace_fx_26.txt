
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return self._linear(x1)

    def _linear(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model(fallback_random=True)
x1 = torch.randn(1, 2, 2)
