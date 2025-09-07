
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1)
        v3  = torch.rand_like(v1).mean() # Note that v3 is not erased from the graph after the `replace_fx` call
__output__  = m(x1)
