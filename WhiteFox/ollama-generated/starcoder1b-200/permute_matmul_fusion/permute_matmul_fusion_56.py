
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t2 = torch.bmm(t1, x2)
        return t2
