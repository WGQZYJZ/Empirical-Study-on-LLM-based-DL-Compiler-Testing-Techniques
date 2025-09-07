
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size):
        v1 = torch.cat([x1, size], dim=1)
        return v1


