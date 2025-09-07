
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self._linear1 = torch.nn.Linear(4, 3)
        self._linear2 = torch.nn.Linear(4, 1)

    def forward(self, x1):
        v1  = torch.cat([x1, x1, x1], dim=-1)
        v1 = torch.relu(v1)
        v1 = self._linear1(v1)
        return self._linear2(v1)


# Initializing the model
m = Model(n=3)

# Inputs to the model
x1 = torch.randn(1, 4, 4)
