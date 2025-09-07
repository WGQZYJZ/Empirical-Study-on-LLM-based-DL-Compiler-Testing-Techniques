
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 20)
 
    def forward(self, x1):
        v1 = torch.flatten(x1, start_dim=1)
        v2 = self.linear(v1)
        v3 = v2 * 0.5
        v4 = (v2 + (v2 ** 3)) * 0.044715
        v5 = v3 * 0.7978845608028654
        v6 = torch.tanh(v4)
        v7 = v5 + 1
        v8 = v2 * v6
        return v8


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
