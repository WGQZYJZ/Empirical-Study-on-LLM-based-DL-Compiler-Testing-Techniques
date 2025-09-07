
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(v0) 
        return v2

