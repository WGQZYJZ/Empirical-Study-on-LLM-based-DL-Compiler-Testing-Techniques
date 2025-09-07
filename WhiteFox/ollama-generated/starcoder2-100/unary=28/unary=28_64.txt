
class Model(torch.nn.Module):
    def __init__(self, min_value=10, max_value=-15):
        super().__init__()
        self.lin  = torch.nn.Linear(32 * 32 * 8, 10)
        self._min_value  = min_value
        self._max_value  = max_value
 
    def forward(self, x1):
        v1  = self.lin(x1.view(-1, 32 * 32 * 8))
        v2  = torch.clamp_min(v1, self._min_value)
        v3  = torch.clamp_max(v2, self._max_value)
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model
 x1  = torch.randn(64, 32 * 32 * 8)
 __output__  = m(x1)