
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear()
 
        self._min  = min_value
        self._max  = max_value
 
    def forward(self, x2):
        v7  = self.linear(x2)
        v8  = torch.clamp_min(v7, 0.)
        v9  = torch.clamp_max(v8, 1.)
        return v9

# Initializing the model
m  = Model()

 # Inputs to the model