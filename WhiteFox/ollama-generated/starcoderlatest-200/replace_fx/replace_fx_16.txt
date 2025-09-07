
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.rand_like(x1, dtype=torch.float) # Will invoke torch.rand_like function for replacement
        t1 = torch.add(v1, 20, dtype=torch.long)     # Will invoke `torch.add` for replacement
        