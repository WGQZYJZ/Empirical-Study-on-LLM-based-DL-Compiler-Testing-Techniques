
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.relu(v1.view(-1, 4))
        v3 = torch.tanh(self.linear1(v2))
        return self.linear2(v3)


# Initializing the model
m = Model()


