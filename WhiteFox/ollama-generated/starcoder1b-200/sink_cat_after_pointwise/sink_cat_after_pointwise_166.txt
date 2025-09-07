
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        return torch.cat([x1, self.relu(x1)], dim=0)


# Initializing the model
m  = Model()


