
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        v = self.linear(x) + 3
        return torch.clamp_min(v, 0).clamp_max(6).div_(6)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 256, requires_grad=True)
y1 = m(x1)
print("X: {}".format(x1))
print("Y: {}".format(y1))

