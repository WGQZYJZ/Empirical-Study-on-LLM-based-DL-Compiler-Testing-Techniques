
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, **kwargs)
        return torch.clamp_max(v2, max_value)

# Initializing the model with maximum value set to 3 and minimum value set to -5
m  = Model(max_value=3, min_value=-5)

 # Inputs to the model 
 x1  = torch.randn(1, 3, 64, 64)
 __output__  = m(x1)

