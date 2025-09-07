
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear()
        self.clamp = torch.nn.Clamp()
 
    def forward(self, x1):
        v2  = self.linear(x1)
        v3  = self.clamp_min(v2, min_value=0.5) 
        v4  = self.clamp_max(v3, max_value=10.)
        return v4
 
# Initializing the model