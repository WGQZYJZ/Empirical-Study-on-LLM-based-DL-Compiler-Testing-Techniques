
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(25, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min=1e-4) # clamp the output of linear to a minimum value of 1e-4
        v3  = torch.clamp_max(v2, max=50) # clamp the output of previous operation to maximum 50
        return v3


# Initializing the model