
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        v3  = self.linear(x2)
        v5  = v3 * 0.5
        v6  = v3 * 0.7071067811865476
        v7  = torch.erf(v6)
        v9  = v7 + 1
        v2  = self._modules['2'](x2, 0) 
        v10 = v5 * v9 # multiplication operation
        v11 = v3 * v10  
        return [v2]


# Initializing the model