
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(10, 3)

    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        t1 = v1 + x2
        return t1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 5)
x2 = torch.randn(10, 3)
