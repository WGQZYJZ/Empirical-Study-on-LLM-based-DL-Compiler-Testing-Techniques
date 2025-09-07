
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5 + (v1 * v1 * v1 * 0.044715) * 0.7978845608028654
        v3 = torch.tanh(v2) + 1
        v4 = v2 * v3
        return v4


# Initializing the model
m = Model()

