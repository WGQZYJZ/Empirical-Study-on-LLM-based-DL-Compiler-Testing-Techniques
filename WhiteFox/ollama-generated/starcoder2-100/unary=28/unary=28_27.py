
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 64 * 64, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1, 32*64*64)) 
        v2  = torch.clamp_min(v1, min_value) # clamped with a minimum value as keyword argument
        v3  = torch.clamp_max(v2, max_value) # clamped with a maximum value as keyword argument
