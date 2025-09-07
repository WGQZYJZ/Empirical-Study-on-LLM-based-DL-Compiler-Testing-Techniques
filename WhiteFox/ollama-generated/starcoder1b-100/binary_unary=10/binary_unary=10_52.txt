
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(16, 12)
        self.relu    = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.linear(x1) + other
        return self.relu(v3)


# Initializing the model
m = Model()

