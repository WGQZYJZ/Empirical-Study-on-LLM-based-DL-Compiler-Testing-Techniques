
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1, dtype=torch.float32)  # rand_like 
        v4  = torch.nn.functional.dropout(v2, p=0.5)   # dropout
        return v4


m = Model()
__output__  = m(x1)

