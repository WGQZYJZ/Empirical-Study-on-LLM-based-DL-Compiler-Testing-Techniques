
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(2)
        v2  = v1.permute(0, 1).reshape(-1, 3)

        return torch.nn.functional.linear(v2, self.linear.weight, bias=None)


m = Model()



