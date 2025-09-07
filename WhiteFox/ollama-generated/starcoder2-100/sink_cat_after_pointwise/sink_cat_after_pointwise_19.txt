
class Model(torch.nn.Module):
    def __init__(self, n=32, m=16):
        super().__init__()

        self._n = torch.nn.Linear(m, 4)
        self._m = torch.nn.Linear(m*5, n)

    def forward(self, x0):
        x1  = self._m(x0).view(-1, 5, m).relu() 
        # concat x1, x2, ... with dim=dim, the result of the concatenation would be t1
        x2 = torch.cat((...), dim=...) # 1 <= dim < ndims(t1)
        t3 = self._n(x2) # use t2 as input for a new operation
        return t3

# Initializing the model