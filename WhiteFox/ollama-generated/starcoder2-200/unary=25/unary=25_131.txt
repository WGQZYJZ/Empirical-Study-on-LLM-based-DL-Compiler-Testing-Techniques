
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x2):
        v7   = self.linear(x2)
        v8   = v7 > 0
        v9   = v7 * negative_slope
        v10  = torch.where(v8, v7, v9)
        return v10
