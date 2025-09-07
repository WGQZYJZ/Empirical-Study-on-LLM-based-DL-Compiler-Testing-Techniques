
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.rand_like(x1, ...)
        x3 = torch.nn.functional.dropout(x1, ...)
        return ...


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(...)
