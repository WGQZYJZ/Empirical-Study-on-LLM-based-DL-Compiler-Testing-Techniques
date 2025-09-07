
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2):
        v1  = torch.mm(x1, y1)
        v2  = torch.mm(x2, y2)
        v3  = v1 + v2
        return v3

# Initializing the model