
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x1[:, :40], x1[:, 63:]], dim=1)
        return v1
 
 