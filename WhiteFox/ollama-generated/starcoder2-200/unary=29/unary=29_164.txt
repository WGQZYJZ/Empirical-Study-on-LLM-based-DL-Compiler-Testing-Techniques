
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value=0.5) 
        v3  = torch.clamp_max(v2, max_value=4.987651687795215e-16) # 1e-18
        return v3

# Initializing the model
m = Model()

