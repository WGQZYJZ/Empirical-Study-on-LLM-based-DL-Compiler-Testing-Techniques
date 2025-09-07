
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...)
        v2 = torch.rand_like(...)
        return v2


# Initializing the model
m = Model()
gm = GraphMatcher()
config['fallback_random'] = True
# Inputs to the model
x1 = torch.randn(1, 2, 2)
