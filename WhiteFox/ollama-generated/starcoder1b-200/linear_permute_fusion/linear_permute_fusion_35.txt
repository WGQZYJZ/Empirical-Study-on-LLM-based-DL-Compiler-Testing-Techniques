
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x1):
        t1 = torch.randn(1, 4, 4)
        v1 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 4)
