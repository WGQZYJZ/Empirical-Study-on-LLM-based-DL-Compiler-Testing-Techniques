
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v = self.linear(x)
        return v * 0.5 + (v * v * v) * 0.044715 + ((v - 0.5)**2 / 2) * 0.7978845608028654 + torch.tanh(v + 1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
