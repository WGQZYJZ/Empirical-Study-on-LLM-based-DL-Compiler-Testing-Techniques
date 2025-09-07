
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3 * 64 * 64, 256)
        self.linear2 = torch.nn.Linear(256, 64)
 
    def forward(self, x1):
        v1 = self.linear1(x1.view(-1))
        v2 = v1 * 0.5
        v3 = (v1 ** 2 + 0.5) * 0.7978845608028654
        v4 = torch.tanh(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
