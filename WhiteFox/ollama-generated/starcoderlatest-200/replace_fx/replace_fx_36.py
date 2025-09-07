
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.dropout(x1, p=0.5)
        v2 = torch.rand_like(v1, 0.) # Random values
        return v2
