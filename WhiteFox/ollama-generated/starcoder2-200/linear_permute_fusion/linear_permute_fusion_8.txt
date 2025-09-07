
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(-1, -2).view(-1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3)
__output__= m(x1)