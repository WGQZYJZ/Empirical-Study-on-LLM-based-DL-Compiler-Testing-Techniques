
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        t1  = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2  = t1.permute(0, 2, 1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
t1 = torch.randn(1, 3, 5)
