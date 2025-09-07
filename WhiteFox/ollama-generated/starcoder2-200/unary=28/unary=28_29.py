
class Model(torch.nn.Module):
    def __init__(self, max_, min_=None):
        super().__init__()
 
        self.lin  = torch.nn.Linear(3*1024, 1)
        self.min_ = None
        self.max_ = max_
 
    def forward(self, x1):
        v1  = self.lin(x1) # Apply linear transformation to input tensor
        v2  = torch.clamp_min(v1, self.min_) # Clamp the output of the linear transformation to a minimum value (if present) or zero by default 
        v3  = torch.clamp_max(v2, self.max_) # Clamp the output of the previous operation to a maximum value
        return v3

m1  = Model(5.)
m2  = Model(-4., max_=0)

