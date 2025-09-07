
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = F.relu6(v2)
        v4  = torch.div(torch.clamp_min(v3, 0), 6)
        return v4


# Initializing the model