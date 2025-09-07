
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1).view(1, -1)
        v2 = v1 * 0.5
        v3 = (v1  + 10 * ((v1 ** 2))) / (v1 ** 2)
        v4 = v3 * 0.7978845608028654
        v5 = torch.tanh(v4)
        v6 = v2 * v5
        return v6

# Initializing the model
m = Model()


