
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(x1) * 3
        v3 = self.linear(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 2)
