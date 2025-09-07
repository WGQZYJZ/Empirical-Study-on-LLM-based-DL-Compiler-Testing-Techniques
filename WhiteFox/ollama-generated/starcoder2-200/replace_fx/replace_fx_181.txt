
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1)
        v2 = torch.rand_like(v1)  # We want to generate random values for the new tensor.
        return v2


m = Model()
__output__  = m(torch.randn(4,3))


