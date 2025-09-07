
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 20)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.randn_like(v1) # <- Other
        return v2

# Initializing the model
m = Model()

