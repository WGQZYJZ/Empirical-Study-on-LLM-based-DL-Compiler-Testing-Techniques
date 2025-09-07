
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
        self.linear2 = torch.nn.Linear(4, 3)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = torch.matmul(v1, v1, v1) * 0.044715
        v3 = v2 + (v2 * v2 * v2) * 0.7978845608028654
        v4 = torch.tanh(v3)
        v5 = torch.matmul(v4, v4, v4) + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
