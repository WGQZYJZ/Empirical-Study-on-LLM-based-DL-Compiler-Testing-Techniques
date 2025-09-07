
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.dropout(x1)
        return torch.rand_like(v2, ...)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.ones(2, 3)
__output__  = m(x1)