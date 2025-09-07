
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1):
        v1 = torch.mm(x1, 5) 
        v2 = torch.mm(y1, -30) 
        v3 = torch.mm(z1, 42) 
        v4 = torch.mm(w1, True) 
        v5 = v1 + v2
        return v3 * v5


# Initializing the model