
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2).permute(0, 2, 1)
        return torch.matmul(v1, self.linear.weight), torch.nn.functional.linear(v2, self.linear.bias)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4)
x2 = torch.randn(1, 2, 2)
__output_1__ = m(x1, x2)
__output_2__ = m(x2, x1)


