
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64, 10)

    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()

