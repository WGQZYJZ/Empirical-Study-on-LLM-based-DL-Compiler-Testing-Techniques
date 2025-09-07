
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = torch.cumsum(x1, 2) 
        return v3

