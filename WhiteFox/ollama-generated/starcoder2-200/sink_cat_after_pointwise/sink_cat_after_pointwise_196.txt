
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v2 = torch.relu(x1.view(-1))
        v3 = v2 * x1

        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5)


