
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp(min=0, max=6, l1 + 3)
        v5 = v4 / 6
        return v5


# Initializing the model