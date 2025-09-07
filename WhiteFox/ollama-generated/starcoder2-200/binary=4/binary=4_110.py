class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2 = v1 + torch.nn.Parameter(data=torch.ones_like(v1), requires_grad=True)
        return v2
