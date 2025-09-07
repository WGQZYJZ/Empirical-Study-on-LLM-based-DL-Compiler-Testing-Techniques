
class Model(torch.nn.Module):
    def __init__(self, min_value=-500, max_value=4096):
        super().__init__()
        self.linear  = torch.nn.Linear(128 * 3, 1)
        self._minval  = -torch.tensor([max_value])
        self._maxval  = torch.tensor([min_value])
 
    def forward(self, x1):
        v0  =  x1 / (1 + abs(x1))
        v2  = self.linear(v0)
        v3  = torch.clamp(v2, self._minval.to(v2), self._maxval.to(v2))
        return v3


# Initializing the model
m  = Model()
__output__  = m(torch.randn(16, 9))

