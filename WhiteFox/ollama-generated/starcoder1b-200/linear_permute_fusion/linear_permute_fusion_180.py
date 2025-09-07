
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = x1.view(x1.shape[0], -1)
        v2 = self.linear(v1)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
