
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5)
        v2 = torch.rand_like(x1)
        return torch.add(v1, v2)


# Initializing the model
m = Model()
__config__ = {'relay.module.fallback_random': False}

# Inputs to the model
x1 = torch.randn(1, 2, 2)
