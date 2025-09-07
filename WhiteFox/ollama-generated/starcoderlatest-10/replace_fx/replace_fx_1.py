
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(x1, requires_grad=True)
        return v1 + v2
