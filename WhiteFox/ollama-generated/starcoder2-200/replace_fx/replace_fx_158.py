class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1)
        t2  = torch.rand_like(t1)
        return t2


m = Model()
x1 = torch.randn(10, 3)

__output__  = m(x1)
