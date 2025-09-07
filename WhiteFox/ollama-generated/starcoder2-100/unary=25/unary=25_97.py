
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = (v1 > 0).float()
        v3 = v1 * negative_slope
        v4 = torch.where(v2 == True, v1, v3)
        return v4


# Initializing the model