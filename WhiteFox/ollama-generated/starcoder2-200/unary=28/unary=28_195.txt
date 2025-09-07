

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = self.__constant0__
        v1  = torch.clamp_min(x1, min=v0)
        v2  = torch.clamp_max(v1, max=v3) 
        return v2


# Initializing the model