
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)

    def forward(self, x1, other=torch.ones((1,))).cuda()
        return self.linear(x1 + other)


# Inputs to the model
x1  = torch.randn(1, 32, dtype=torch.double).cuda()
__output__  = m(x1)

