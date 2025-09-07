
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2 = v1 - 5000
        v3 = torch.nn.functional.relu(v2)
        return v3


m = Model()
x1 = torch.randn(4, 8)
out_0 = m(x1)


