
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x):
        v = x.permute(0, 2, 1)
        return self.linear(v)


# Inputs to the model
x = torch.randn(1, 2, 4)
__output = Model()(x)

