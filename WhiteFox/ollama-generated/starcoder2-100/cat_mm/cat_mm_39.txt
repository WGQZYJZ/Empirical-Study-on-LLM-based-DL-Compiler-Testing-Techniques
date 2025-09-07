
class Model(torch.nn.Module):
    def __init__(self, dim=10):
        super().__init__()
        self.dim  = dim
 
    def forward(self, x1, y2):
        v1  = torch.mm(x1, y2)
        v2  = torch.cat([v1 for _ in range(self.dim)])
        return v2


# Initializing the model