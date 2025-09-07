
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu  = torch.nn.ReLU()

    def forward(self, x1):
        v1  = x1 + x2
        v2  = torch.cat([x1, x2], dim=0)
        v3 = self.relu(v2)
        return v3


# Initializing the model
m = Model()


