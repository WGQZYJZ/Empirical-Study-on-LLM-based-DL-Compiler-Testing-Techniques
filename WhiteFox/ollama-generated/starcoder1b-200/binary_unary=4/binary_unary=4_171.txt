
class Model(torch.nn.Module):
    def __init__(self, other=1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x):
        v = self.linear(x) + self.other
        v = relu(v)
        return v


# Initializing the model
m = Model()
