
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=10):
        super().__init__()
        self.hidden = torch.nn.Linear(2,  hidden_dim)

    def forward(self, x1, x2):
        v1 = x1 + x2
        v2 = self.hidden(v1)
        return v2


# Initializing the model