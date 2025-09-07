
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        v = torch.nn.functional.linear(input1)
        return torch.nn.functional.conv2d(v, 3)


m  = Model()

x1 = torch.rand([16, 90])
__output__  = m(x1)