
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5)
        t2 = torch.rand_like(x1)
        return t1 + t2


# Inputs to the model
x1 = torch.randn(2, 3, 4)
