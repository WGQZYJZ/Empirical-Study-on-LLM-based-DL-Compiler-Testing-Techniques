
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 > 0
        v3  = negative_slope = 0.5
        v4  = v1 * v3
        v5  = torch.where(v2, v1, v4)
        return v5
