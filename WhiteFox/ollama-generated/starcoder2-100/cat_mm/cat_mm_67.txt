
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2) 
        v2 = torch.cat([v] * len(range(size)), dim=0) # concatenation along a specified dimension
        return v2


# Initializing the model