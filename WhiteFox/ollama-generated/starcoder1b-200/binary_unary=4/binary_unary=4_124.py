
class LinearModel(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(50, 1)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x):
        v = self.linear(x) + other
        v = self.relu(v)
        return v


# Initializing the model
m = LinearModel()


