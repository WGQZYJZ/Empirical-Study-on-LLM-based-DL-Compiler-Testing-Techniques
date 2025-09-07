

class Model(torch.nn.Module):
    def __init__(self, min_value=-20, max_value=10):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=max_value) 
        v3  = torch.clamp_max(v2, max=-min_value)    
        return v3
