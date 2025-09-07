
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, t1, t2):
        v1 = torch.cat([t1, t2], dim=-1)
        v2 = self.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
t1 = torch.randn(3, 2)
t2 = torch.randn(3, 2)
