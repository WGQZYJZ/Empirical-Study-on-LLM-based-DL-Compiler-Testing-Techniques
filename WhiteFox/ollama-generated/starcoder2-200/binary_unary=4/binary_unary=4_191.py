
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear  = torch.nn.Linear(3*64*64, 1)
        self._other = other
 
    def forward(self, x1):
        v1  = self.linear(x1).flatten()
        if (self._other is not None):
            v2  = v1 + self._other
        else: 
            v2  = torch.zeros_like(v1)
        v3  = F.relu(v2)
        return v3


# Initializing the model, setting up the keyword argument `other` to be a vector of size 4096
m  = Model(torch.ones(1, 4096))

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
  __output__  = m(x1)

