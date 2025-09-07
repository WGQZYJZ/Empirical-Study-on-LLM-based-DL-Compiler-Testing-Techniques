
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.linear2 = torch.nn.Linear(64, 10)
 
    def forward(self, x1):
        v1 = self.linear1(x1) * 0.5
        v2 = self.linear2(v1) + ((self.linear1(v1)) ** 3) * 0.044715
        v3 = v2 * 0.7978845608028654
        v4 = torch.tanh(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


