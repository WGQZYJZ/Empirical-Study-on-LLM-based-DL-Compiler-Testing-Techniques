
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, split_sizes, dim)
        v2 = torch.cat([v for v in v1], dim)
        return v2
