
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()
# Note that `other` is not set here
