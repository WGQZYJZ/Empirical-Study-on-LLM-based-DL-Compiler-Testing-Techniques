
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.25)
        t2 = torch.rand_like(x1)

        return t2 + t1

# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(20, 32, 32)
output = m(__input__)

