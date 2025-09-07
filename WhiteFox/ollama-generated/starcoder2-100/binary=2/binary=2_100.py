class Model(torch.nn.Module):
    def __init__(self,  other: torch.Tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other # 'other' is assigned a tensor or scalar variable in the class body 
        return v2
