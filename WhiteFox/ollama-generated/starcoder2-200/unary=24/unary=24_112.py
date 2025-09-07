class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2513964837536001)
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).type_as(v1) 
        v3  = negative_slope * torch.clamp(-v1*v2 + v1, min=0) + v2
        return v3
