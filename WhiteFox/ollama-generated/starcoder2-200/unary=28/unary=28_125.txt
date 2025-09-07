
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min(-40)) # Clamp the output of the linear transformation to a minimum value
        v3  = torch.clamp_max(v2, max(-8)) # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model