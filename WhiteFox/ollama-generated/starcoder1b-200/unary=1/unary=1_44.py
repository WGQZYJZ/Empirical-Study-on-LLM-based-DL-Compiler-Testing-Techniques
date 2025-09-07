
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = (v1 + 0.044715 * torch.pow(torch.sqrt(torch.abs(v1)), 3)).mul(0.7978845608028654)
        v4 = v3.tanh()
        v5 = v2 * v4
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2048)
