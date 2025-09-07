
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = v1 * 0.5
        v3 = (v1 ** 3).sum()
        v4 = torch.tanh(v2) + 1
        v5 = v3 * v4
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3 * 64 * 64)
