
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5)
        v2 = torch.rand_like(v1)
        return torch.cat([v1, v2], dim=0)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3, requires_grad=True)
