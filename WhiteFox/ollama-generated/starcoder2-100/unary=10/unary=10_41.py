# Initializing the model with initial weights and bias terms
weights = torch.ones(32, 10) / np.sqrt(32 + 10)
bias = torch.zeros(32)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(784, 32, bias=False)
        self.lin.weight.data = weights
        self.lin.bias.data = bias
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        v5  = v4 / 6
        return v5
