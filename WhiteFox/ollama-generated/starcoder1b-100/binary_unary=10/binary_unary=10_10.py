
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)

    def forward(self, x):
        v = self.linear(x) + 2
        return relu(v)


# Initializing the model
m = Model()

