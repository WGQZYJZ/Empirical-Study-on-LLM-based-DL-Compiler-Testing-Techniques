
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.linear(x1, ...)
        v2 = t1.permute(...)
        return v2
