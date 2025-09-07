
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 2)

    def forward(self, x):
        v1 = torch.cat([x, x], dim=1)
        v2 = v1.view(v1.shape[0], -1)
        v3 = torch.relu(v2)
        return self.linear2(torch.relu(self.linear1(v3)))

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 64, 8, 8)
