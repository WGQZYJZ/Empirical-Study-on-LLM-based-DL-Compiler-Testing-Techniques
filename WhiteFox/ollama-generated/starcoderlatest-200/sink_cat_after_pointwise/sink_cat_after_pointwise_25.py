
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(4, 3)

    def forward(self, x1, x2, x3):
        v1 = x1 + x2
        v2 = torch.cat([v1, v1 * x2], dim=0) # Note that this pattern is detected in the model!
        v3 = torch.relu(torch.nn.functional.linear(v2, self.linear1.weight, self.linear1.bias))
        return torch.sigmoid(self.linear2(v3))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 1, 5)
x2 = torch.randn(20, 2, 5)
