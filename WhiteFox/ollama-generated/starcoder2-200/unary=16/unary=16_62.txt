
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(128 * 7 + 3, 4096)

    def forward(self, x1):
        v1 = self.layer(x1)
        v2 = F.relu(v1)

        return v2

# Initializing the model