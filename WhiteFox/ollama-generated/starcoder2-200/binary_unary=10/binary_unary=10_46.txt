
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 32, 10)
        self._other = torch.nn.Linear(64 * 32, 10)(x1).sum()
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        return v1 + self._other

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(32 * 64, 10)

