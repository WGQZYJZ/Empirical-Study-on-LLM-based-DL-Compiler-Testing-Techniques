
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v7 = torch.cat([x2[:, :3], x2[:, 5:8]], dim=1)
        return v7

