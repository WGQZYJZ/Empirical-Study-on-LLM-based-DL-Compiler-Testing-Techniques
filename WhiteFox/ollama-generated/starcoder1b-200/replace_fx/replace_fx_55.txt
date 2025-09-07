
class Model(torch.nn.Module):
    def __init__(self, opts={}):
        super().__init__()

    def forward(self, x1):
        x2 = torch.rand_like(x1, 0)
        return x2

