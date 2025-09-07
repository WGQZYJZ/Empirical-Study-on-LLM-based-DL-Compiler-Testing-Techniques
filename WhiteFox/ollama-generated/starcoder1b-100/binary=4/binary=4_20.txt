
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=3, out_features=10)

    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model(torch.randn((1, 10)))


