
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.3)
        v2 = torch.rand_like(x1, dtype=v1.dtype)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 4, 3)
