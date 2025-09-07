
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear.weight @ v1 + self.linear.bias
        return v2

m = Model()
inputs = torch.randn(1, 2, 2)
__output = m(inputs)

