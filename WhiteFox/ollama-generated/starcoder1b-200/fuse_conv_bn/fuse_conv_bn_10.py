
class Model(torch.nn.Module):
    def __init__(self, features, hidden):
        super().__init__()
        self.linear1 = torch.nn.Linear(features, hidden)
        self.linear2 = torch.nn.Linear(hidden, 1)

    def forward(self, x):
        out = torch.relu(self.linear1(x))
        out = self.linear2(out)
        return out


# Initializing the model
m = Model(3, 5)


# Inputs to the model
x1 = torch.randn(1, 3, 4)
