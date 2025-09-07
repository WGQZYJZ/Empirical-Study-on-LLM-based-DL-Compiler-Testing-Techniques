
class Model(torch.nn.Module):
    def __init__(self, other=2):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 50)
        self.linear2 = torch.nn.Linear(50, 10)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()
other = torch.randn(784)
