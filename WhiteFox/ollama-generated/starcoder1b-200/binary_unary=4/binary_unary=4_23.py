
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.relu   = torch.nn.ReLU()
        self.add    = torch.nn.Add()
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + other if not other is None else x1
        v3 = self.relu(v2)
        return v3


# Initializing the model
m = Model(other=torch.randn(1, 3))

