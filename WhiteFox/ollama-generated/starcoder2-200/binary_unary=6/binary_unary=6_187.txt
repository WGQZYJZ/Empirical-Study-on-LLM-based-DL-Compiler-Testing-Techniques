
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(3,4)

    def forward(self, x):
        v1  = self.lin1(x)
        v2  = v1 - other
        v3  = torch.relu(v2)
        return v3

# Initializing the model