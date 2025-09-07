
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 3)

    def forward(self, x):
        v1 = torch.nn.functional.linear(x, self.linear1.weight, self.linear1.bias)
        v2 = v1.permute(-1, -2).contiguous()
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 5)
__output__  = m(x1)
