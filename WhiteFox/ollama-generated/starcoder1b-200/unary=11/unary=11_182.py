
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        return (v3 / 6).contiguous()


# Initializing the model
m = Model()


