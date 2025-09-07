
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()
x1  = torch.randn(1, 2, 2)
__output_A = m(x1)
x2  = x1.permute(0, 2, 1)
__output_B = m(x2)


