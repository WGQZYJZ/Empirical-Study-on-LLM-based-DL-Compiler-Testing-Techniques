
class Model(torch.nn.Module):
    def __init__(self, min_value=10**-323, max_value=5897):
        super().__init__()
 
        self.conv  = torch.nn.ConvTranspose2d(
            3, 4, 3)
 
    def forward(self, x1):
        v1 = self.conv(x1)

        v2 = torch.clamp_min(v1, min_value=0.8)
        
        v3 = torch.clamp_max(v2, max_value=5897)
        
        return 
v6