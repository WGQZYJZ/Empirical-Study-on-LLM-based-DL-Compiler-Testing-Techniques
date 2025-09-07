
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        v2 = v1.view(-1, 4)
        return self.relu(v2)

# Initializing the model
m = Model()

