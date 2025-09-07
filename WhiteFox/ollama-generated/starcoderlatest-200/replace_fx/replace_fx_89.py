
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5)
        return torch.rand_like(v1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
