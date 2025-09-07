
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.clamp_max(x1, max=5) # clamp the input to a maximum value of 5
        v2  = v1 + 6
        return v2


# Initializing the model