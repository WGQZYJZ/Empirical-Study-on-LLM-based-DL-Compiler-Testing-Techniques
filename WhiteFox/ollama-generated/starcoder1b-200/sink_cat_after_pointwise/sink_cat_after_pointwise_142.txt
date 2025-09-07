
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.view(-1, 4)
        v2 = torch.relu(self.linear(v1))
        return v2


# Initializing the model
m = Model()


