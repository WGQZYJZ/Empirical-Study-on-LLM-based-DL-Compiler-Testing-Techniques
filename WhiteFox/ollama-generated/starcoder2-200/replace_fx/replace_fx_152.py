
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.nn.functional.dropout(x1 + torch.rand_like(x1), 0.5)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 2)
__output__  = m(x1)

