

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(1)
 
    def forward(self, key, value):
        v  = torch.matmul(self.scale * query , key.transpose(-2,-1))
        return v

# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(64)
key    = torch.randn(30, 30) # Must be of shape [L, Q], L and Q are length of key and query vector.
value  = torch.randn(29851712, 64)
 
__output__  = m(query, value, key)

