
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.rand_like(x1)
        t2 = torch.nn.functional.dropout(t1, ...)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 5)
