
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.nn.functional.dropout(x1)
        v4 = torch.nn.functional.dropout(v3)
        return torch.rand_like(v4, dtype=torch.int64)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2560, 9)
__output__  = m(x1)