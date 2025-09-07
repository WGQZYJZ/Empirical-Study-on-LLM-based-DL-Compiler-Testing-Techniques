
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = self.mm(x1, x2)
        # v1 is concatenated with v1 at the specified dimension

        v2 = torch.cat([v1, v1, ..., v1], dim=-1)
        return v2

    def mm(self, x1, x2):
        