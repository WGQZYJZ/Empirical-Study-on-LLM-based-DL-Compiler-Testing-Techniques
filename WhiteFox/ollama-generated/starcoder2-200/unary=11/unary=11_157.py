
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # This is to indicate the starting point of the model
        v2 = self._conv(x1) + 3 
        v3 = torch.clamp_min(v2, 0)   
        v4 = torch.clamp_max(v3, 6)  
        return torch.div(v4, 6)


# Initializing the model and defining an entry point (starting point of the model)
m = Model()
__output__  = m(x1)
