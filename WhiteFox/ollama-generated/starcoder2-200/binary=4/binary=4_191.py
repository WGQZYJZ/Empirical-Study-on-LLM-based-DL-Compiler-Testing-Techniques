
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*8+3, 1)
 
    def forward(self, x1):
        v0  = self._prepare_input(x1)
        return self.linear(v0)
        
    def _prepare_input(self, x):
      return x

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(64*32*8, 1)
xother = torch.randn(57909 + 64 * 32 * 8)
__output__  = m(x1, other=xother)
