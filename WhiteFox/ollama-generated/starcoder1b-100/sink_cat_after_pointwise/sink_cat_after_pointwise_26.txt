
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        return self.linear1(v1), self.linear2(v2)


# Inputs to the model
x1 = torch.randn(1, 3, 4)
x2 = torch.randn(1, 2, 4)
__output1__ = m(x1, x2)
__output2__ = m(x2, x1)


