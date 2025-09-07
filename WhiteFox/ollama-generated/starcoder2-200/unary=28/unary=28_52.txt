
class Model(torch.nn.Module):
    def __init__(self, min_, max_=1024):
        super().__init__()
        self.linear  = torch.nn.Linear(3*64*64, 78)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_)
        v3  = torch.clamp_max(v2, max_)
 
        return v3


# Initializing the model
m  = Model(-50.)
__output__   = m(torch.zeros(1, 3*64*64))

