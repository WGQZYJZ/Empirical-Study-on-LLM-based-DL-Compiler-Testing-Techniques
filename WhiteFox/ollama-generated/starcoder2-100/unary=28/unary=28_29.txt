
class Model(torch.nn.Module):
    def __init__(self, max_=None, min_=None):
        super().__init__()
        self.conv  = torch.nn.Linear()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=min_)
        v3  = torch.clamp_max(v2, max_=max_) 
        return v3

# Initializing the model
m = Model(max_=None, min_=None)

