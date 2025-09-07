class Model(torch.nn.Module):
    def __init__(self, m: int):
        super().__init__()
 
    def forward(self, x1, y2):
        v1 = torch.mm(x1, y2)
        v2  = torch.cat([v1] * (m // 3), -1)
        return v2
