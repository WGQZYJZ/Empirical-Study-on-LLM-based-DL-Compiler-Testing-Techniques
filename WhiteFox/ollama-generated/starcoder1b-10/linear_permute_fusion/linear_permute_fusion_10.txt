
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x1):
        v1  = x1.permute(1, 2, 0)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 10)
