
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(16, 3200)
    
    def forward(self, x1):
            v1 = self.lin(x1)
            v2 = v1 * clamp(min=0, max=6, v1 + 3)
            v3 = v2 / 6
            return v3


# Initializing the model