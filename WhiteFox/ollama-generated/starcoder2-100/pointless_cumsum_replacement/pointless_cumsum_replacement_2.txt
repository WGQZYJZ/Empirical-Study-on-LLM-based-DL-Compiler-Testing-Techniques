
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, v0):
        return torch.cumsum(v0 + 1, dim=1)

