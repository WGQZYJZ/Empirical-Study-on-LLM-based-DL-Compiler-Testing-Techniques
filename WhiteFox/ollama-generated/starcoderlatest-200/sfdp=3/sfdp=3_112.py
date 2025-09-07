
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(128, 64)
 
    def forward(self, x1, x2):
        v1 = self.matmul(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6, v5, v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 10, 64)
x2 = torch.randn(1, 16, 64)
__output__, __t_5__, __t_4__ = m(x1, x2)


