
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3,8,1)
        self.clamp1  = torch.nn.functional.relu()
        self.clamp2  = torch.nn.functional.relu()
 
    def forward(self, x):
        v1  = self.convT(x)
        v2  = self.clamp1(v1) # clamping min value
        v3  = self.clamp2(v2) # clamping max value
        return v3

# Initializing the model