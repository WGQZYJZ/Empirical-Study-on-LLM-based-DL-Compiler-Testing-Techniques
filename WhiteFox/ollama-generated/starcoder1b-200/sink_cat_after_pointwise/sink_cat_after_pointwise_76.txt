
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = self.relu(v1)
        return v2


# Initializing the model
m = Model()

