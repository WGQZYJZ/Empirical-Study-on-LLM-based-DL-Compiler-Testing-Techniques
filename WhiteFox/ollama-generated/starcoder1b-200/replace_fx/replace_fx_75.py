
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return self.linear(x1)


m1 = Model()
m2 = Model()

# Initializing models
m1.eval()
m2.eval()

with torch.no_grad():
    x1 = torch.randn(1, 2, 2)
    x2 = m1(x1)

    