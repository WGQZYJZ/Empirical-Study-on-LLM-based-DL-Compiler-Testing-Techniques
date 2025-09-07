
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x):
        t1 = torch.nn.functional.linear(x, self.linear.weight, self.linear.bias)
        t2 = t1.permute(0, 3, 1, 2)
        return t2


# Initializing the model
m = Model()


# Inputs to the model