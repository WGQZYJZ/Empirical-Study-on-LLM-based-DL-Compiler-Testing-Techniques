
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * F.relu6(v1 + 3)
        v3 = v2 / 6

        return v3

m = Model()

# Inputs to the model
x1 = torch.randn(4, 10)
__output__  = m(x1)