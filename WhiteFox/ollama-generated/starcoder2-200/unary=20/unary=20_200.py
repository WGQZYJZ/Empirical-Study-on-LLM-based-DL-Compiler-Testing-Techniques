
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.randn(5) * self._float_range[0] + self._float_range[1] # Normal distribution of floats in range
        self.