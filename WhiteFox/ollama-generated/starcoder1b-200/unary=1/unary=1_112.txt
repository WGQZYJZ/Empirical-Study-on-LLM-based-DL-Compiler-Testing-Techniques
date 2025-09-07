
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5 + (v1 * v1 * v1) * 0.044715
        v3 = v2 * 0.7978845608028654
        v4 = torch.tanh(v3) + 1
        return v4


# Initializing the model
m = Model()


