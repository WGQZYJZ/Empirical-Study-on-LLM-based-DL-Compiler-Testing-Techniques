
class Model(torch.nn.Module):
    def __init__(self, min_value=10., max_value=-20.):
        super().__init__()
 
    def forward(self, x):
        v = self.linear(x) 
        v  = torch.clamp(v, min=min_value) # clamp output of linear transformation to a minimum value
        v  = torch.clamp(v, max=max_value) # clamp output of the previous operation to a maximum value
        return v

# Initializing the model