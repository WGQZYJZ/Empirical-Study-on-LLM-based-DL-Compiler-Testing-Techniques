class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.qk   = torch.nn.Linear(in_features=64*64*8, out_features=10000)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.transpose(v1, -2, -3) 
        v3  = v2 @ v2
        v5  = v2 @ v2 * 0.7071067811865476 / math.sqrt(query.size(-1))
        v4  = torch.erf(v3) + 1 
        v6  = v5 - v4
        v7  = torch.nn.Dropout(p=0)(v6) 
        return v7
 
