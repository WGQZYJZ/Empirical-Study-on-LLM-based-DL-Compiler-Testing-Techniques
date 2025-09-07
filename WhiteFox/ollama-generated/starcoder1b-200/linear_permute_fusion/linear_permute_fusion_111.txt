
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        return self.linear(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
