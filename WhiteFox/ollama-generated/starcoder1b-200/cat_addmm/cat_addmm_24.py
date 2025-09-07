
class Model(torch.nn.Module):
    def __init__(self, x1_shape):
        super().__init__()
        self.x1 = torch.randn(*x1_shape)
 
    def forward(self):
        v1 = self.x1
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v1 * v5
        return v6


# Initializing the model
m = Model(x1_shape=(2, 2, 1))


# Inputs to the model
x1 = torch.randn(2, 2, 1, 2)
v1 = m(x1)
