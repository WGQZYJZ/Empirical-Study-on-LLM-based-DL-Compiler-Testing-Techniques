
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v0 = torch.full([arg1, arg2], 1, dtype=torch.int64)
        v0 = torch.tensor(v0).type(dtype)
        v3 = torch.cumsum(v0, dim=1)
        return v3
