
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)

    def forward(self, x1):
        v1 = torch.tensor([[1.0 / math.sqrt(2), -1.0 / math.sqrt(2)],
                           [-1.0 / math.sqrt(2), 1.0 / math.sqrt(2)]])
        v2 = sigmoid(self.linear(x1))
        return v3 * v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 784)
