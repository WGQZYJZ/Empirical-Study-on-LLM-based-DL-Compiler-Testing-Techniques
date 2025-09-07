
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64, 1)

    def forward(self, x1):
        v0  = self.linear(x1)
        v1  = v0 * 0.5
        v2  = (v0 * v0 * v0) * 0.044715 + v1
        v3  = v2 * 0.7978845608028654
        v4  = torch.tanh(v3)
        v5  = v4 + 1 
        return v5


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 64)
__output__  = m(x1)
