
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2=None):
        if x2 is None:
            v1 = torch.nn.functional.dropout(x1, p)
        else:
            v2  = torch.rand_like(x2)
        return v2


# Inputs to the model
x1 = torch.randn(100, 20)
