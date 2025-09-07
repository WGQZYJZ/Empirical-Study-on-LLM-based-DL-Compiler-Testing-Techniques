
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 20)
 
    def forward(self, x1):
        v1 = self.linear(x1) * 0.5
        v2 = v1 + ((v1 ** 2) * 0.044715)
        v3 = (v2 ** 2) * 0.7978845608028654
        v4 = torch.tanh(v3) + 1
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 32, 32)
