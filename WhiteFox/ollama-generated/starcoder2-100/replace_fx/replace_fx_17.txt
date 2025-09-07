
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x):
        v1 = torch.nn.functional.dropout(x, 0.35)
        return torch.rand_like(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 2)

__output__  = m(x1).mean().item()

