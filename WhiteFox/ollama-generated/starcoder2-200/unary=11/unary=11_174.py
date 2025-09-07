

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x):
        v0  = self.conv(x) 
        v1  = v0 + 3 
        v2  = torch.clamp_min(v1, 0)
        v3  = torch.clamp_max(v2, 6) 
        v4  = v3 / 6    
        return v4
