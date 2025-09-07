
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(v1)
        return v2


# Generating the model from scratch
m = torch.jit.script(Model())

# Inputs to the model
x1 = torch.randn(1, 2, 2)
