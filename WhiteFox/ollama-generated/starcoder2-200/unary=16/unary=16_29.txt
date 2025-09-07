

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.layer1 = torch.nn.Linear(5000, 2)

    def forward(self, x):
        v1  = self.layer1(x)

        return torch.relu(v1)

model = Model()

