class Model(torch.nn.Module):
    def __init__(self, len1=30, len2=8):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1] * len2, dim=-1)
        return v2
