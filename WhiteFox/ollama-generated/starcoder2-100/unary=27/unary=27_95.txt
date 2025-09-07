
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, -10)
        v3  = torch.clamp_max(v2, 50) 
        return v3


# Initializing the model and generating inputs to the model