

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 - other # here!
        v3 = F.relu(v2)
        return v3

m = Model()
other  = torch.randn(1).item() + 50

# Inputs to the model