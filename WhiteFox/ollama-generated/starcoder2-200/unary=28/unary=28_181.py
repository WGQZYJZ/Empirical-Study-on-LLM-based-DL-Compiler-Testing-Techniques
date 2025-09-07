class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v0  = self.linear(x1) # apply a linear transformation to the input tensor
        v2  = torch.clamp_min(v0, -15.)  # clamp to minimum value
        v4  = torch.clamp_max(v2, 339978.)  # clamp to maximum value 
        return v4
