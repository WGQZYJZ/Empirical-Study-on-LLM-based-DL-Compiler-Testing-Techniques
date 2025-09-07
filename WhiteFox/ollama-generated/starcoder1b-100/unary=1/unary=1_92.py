
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) * 0.5
        v2 = (self.linear(x1) + 0.044715) * 0.7978845608028654
        v3 = torch.tanh(v2)
        v4 = v3 + 1
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 128)
