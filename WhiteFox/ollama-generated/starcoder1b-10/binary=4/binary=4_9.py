
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 5)

    def forward(self, x1):
        x2 = x1 * 0.25
        other = torch.randn(5)
        return self.linear1(x2) + other


# Initializing the model
m = Model()


