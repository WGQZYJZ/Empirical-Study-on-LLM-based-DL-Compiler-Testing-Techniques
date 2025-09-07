
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.linear = torch.nn.Linear(1280, 4)
        self._min = min_(123.)
        self._max = max_(567.)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp_min_(v1)
        v3 = clamp_max_(v2)
        return v3


# Initializing the model
m  = Model(torch.clamp_min_, torch.clamp_max_)

 # Inputs to the model
x1  = torch.randn(1, 1280)
  __output__  = m(x1)
