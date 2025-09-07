
class Model(torch.nn.Module):
    def __init__(self, opt=None):
        super().__init__()

        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3, x4):
        t1 = torch.cat([x1, x2, x3, x4], dim=0)
        v1 = self.linear(t1)
        return v1


# Initializing the model and setting the optimizer to None, as the optimization cannot be inferred from the model's forward function.
m = Model()
_ = m  # Raises a TypeError, because of the missing argument `opt`.
opt = optim.SGD(...)
m = Model(opt)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
x3 = torch.randn(1, 2, 2)
x4 = torch.randn(1, 2, 2)
