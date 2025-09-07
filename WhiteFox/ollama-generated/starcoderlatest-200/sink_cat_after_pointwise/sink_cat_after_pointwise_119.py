
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=0)
        v1 = t1.view(-1, 4)
        return torch.relu(v1)
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(2, 2, 2)
