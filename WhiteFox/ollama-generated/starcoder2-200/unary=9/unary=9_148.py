
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2,0).clamp_max(6,7) # Clamp_min_test.py
        v4  = v3 / 6
return v4

# Initializing the model