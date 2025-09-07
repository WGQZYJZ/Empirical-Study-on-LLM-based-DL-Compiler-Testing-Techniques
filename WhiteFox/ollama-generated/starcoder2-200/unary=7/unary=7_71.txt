
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 * F.clamp(v1 + 3, min=0, max=6)
        v3 = v2 / 6
        return v3

# Initializing the model