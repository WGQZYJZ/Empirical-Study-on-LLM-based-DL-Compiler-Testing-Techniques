
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)

    def forward(self, x2):
        v3  = self.linear(x2)
        v5  = torch.tanh(v3)

        return v5

# Initializing the model