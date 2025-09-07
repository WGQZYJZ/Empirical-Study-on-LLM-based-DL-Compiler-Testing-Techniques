
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.25, True)
        t2 = torch.rand_like(t1, 0.25)
        return t2


# Input data to the model
x1 = torch.randn(1, 3, 64, 64)
