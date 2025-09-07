
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.linear(x1)
        return v1.permute(0, 2, 1)


# Initializing the model
m = Model()


# Inputs to the model
t1 = torch.randn(1, 3, 3)
