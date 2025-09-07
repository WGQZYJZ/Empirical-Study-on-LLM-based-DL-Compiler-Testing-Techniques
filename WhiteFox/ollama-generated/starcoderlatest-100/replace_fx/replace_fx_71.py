
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.3)
        v2 = torch.rand_like(x1)
        return (v1 + v2).max()


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 4)
