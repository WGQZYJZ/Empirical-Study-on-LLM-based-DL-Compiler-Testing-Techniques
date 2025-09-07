
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
         v1 = self.conv(x) + 0.5
         v4 = v1 * 0.7071067811865476
        v2  = torch.clamp_min(v4, min=0.)
         v3  = torch.clamp_max(v2, max=0)
         return v3


# Initializing the model