
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x):
        v = self.linear(x)
        v = v * 0.5
        v += (v * v * v) * 0.044715
        v *= 0.7978845608028654
        return torch.tanh(v) + 1


# Initializing the model
m = Model()


