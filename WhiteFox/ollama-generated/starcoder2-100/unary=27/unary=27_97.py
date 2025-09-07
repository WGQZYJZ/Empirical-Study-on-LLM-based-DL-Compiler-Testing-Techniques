
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v2 = torch.clamp_min(v3, min=0)
         v4  = self.conv(x1).clamp_max(63)
         return v4
# Initializing the model
m = Model()

 # Inputs to the model