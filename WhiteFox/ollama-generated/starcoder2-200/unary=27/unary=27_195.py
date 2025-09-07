
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v2  = torch.clamp_min(v1, min)
         v3  = torch.clamp_max(v2, max)
         return v3

# Initializing the model