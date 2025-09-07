
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.nn.functional.relu(v1)
        return torch.sigmoid(torch.matmul(v2, self.linear2.weight))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 2)
