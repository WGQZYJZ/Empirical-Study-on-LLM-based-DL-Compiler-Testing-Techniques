
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = torch.relu(v1)
        return self.linear(torch.relu(torch.cat([v2, x3], dim=0)))


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
x3 = torch.randn(1, 4, 2)
