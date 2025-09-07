
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1  = torch.nn.Linear(32, 8)

    def forward(self, x1):
        v0 = self.l1(x1)
        return (v0 + 3).clamp(min=0, max=6)/6

# Initializing the model
m = Model()

# Input tensor to the model
x1 = torch.randn(256, 32)

