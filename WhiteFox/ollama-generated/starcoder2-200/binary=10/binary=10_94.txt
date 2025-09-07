
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)

    def forward(self, x):
        v0 = other
        v1 = self.linear(x) + v0 
        return v1


# Initializing the model