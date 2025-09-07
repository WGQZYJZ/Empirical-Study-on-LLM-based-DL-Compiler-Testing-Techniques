
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(25, 4)
        self.fc2 = torch.nn.Linear(4, 10)

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1], dim=1)
        return self.fc2(torch.tanh(self.fc1(v2)))


# Initializing the model
m = Model()

