
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, 4)
        t3 = torch.relu(t2)
        v2 = self.linear(t3)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 2)
x2 = torch.randn(4, 2, 2)
