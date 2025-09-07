class MyModel(nn.Module):
    def __init__(self, n):
        super().__init__()

    def forward(self, x1):

        t3 = torch.mm(x2, x3)
        t4 = torch.cat([t3] * 50 + [x4], dim=1)
        return t4
