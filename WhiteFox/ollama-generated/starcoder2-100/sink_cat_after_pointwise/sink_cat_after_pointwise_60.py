
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.relu(x1)
        v3 = torch.cat([v2, x1], dim=0).view(-1, 5)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model