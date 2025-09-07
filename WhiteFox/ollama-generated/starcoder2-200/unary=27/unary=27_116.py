
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.min = 0.5
        self.max = 99
    
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp_min(v1, min=self.min) 
        return torch.clamp_max(v2, max=self.max)
# Initializing the model
m  = Model()
