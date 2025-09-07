
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v0  = self.linear(x1)
        v1  = (v0 > 0).float()
        v2  = negative_slope * v0 
        v3  = v2 + ((~v1) & torch.abs(v0))
        return v3


# Initializing the model