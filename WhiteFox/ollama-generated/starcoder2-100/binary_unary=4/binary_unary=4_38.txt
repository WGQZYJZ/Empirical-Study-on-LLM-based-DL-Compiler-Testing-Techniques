
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x1):
        v1 = self.linear(x1) 
        return v1 + other

# Initializing the model