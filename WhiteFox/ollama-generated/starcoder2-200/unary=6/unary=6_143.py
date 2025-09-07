class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3 
        v2  = torch.clamp_min(v1, 0 ) / 6
        return v2
