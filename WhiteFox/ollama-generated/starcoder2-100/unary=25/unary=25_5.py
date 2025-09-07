

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64, 1)
 
    def forward(self, x2):
        v7 = self.linear(x2)
        v9 = v7 > 0
        v10 = negative_slope = float(1e-3)
        v11 = v7 * v10
        v12 = torch.where(v9, v7, v11)
        return v12


# Initializing the model