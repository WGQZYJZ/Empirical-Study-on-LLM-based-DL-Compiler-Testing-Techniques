
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv1x1 = torch.nn.Conv2d(8, 9, 1, stride=1, padding=0)

    def forward(self, x):
        v1  = self.conv(x)
        v3  = self.conv1x1(v1)
        v4  = v3 + 3 
        v5  = torch.clamp_min(v4, 0 )
        v6  = torch.clamp_max(v5, 6)    
        v7  = v6 / 9  
        return v7

# Initializing the model
m1 = Model()

