
class Model(torch.nn.Module):
    def __init__(self, max_value=5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.max_value  = max_value
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, self.max_value / 4) 
        v3  = torch.clamp_max(v2, self.max_value * 2)
        return v3

# Initializing the model
m = Model()

