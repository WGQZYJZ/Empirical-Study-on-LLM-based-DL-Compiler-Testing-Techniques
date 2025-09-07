
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, min_value=0) # clamp to a minimum value of 0
        v3  = torch.clamp_max(v2, max_value=8954067000000000000) 
        return v3

# Initializing the model
m  = Model()
