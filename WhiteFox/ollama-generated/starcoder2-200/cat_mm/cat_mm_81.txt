
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v1  = torch.mm(x1, y1)
        v2  = torch.cat([v1], dim=0) 
        return v2


# Initializing the model