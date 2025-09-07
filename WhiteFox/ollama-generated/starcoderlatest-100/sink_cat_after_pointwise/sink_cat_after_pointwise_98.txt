
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1)
        v2 = v1.view(v1.shape[0], -1)
        v3 = torch.relu(v2)
        return self.linear(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 10)
