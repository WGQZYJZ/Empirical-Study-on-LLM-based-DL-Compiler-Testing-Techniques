
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(4, 8)
        self.fc2 = torch.nn.Linear(8, 3)

    def forward(self, x1):
        t1 = self.fc1(x1)
        t2 = self.fc2(t1)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8)
