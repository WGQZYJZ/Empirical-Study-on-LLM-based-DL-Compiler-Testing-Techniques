
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = torch.relu(x1[:, 0])
        v2 = torch.sigmoid(x1[:, 1])
        v3 = torch.tanh(v1 + v2)
        return self.linear(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
