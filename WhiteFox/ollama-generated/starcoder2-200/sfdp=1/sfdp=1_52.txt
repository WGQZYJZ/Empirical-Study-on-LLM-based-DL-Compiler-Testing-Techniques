
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(64, 32)
 
    def forward(self, query, key, value):
        v1  = self.attention(query, key, value)[0]
        return v1

# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(8, 64)
k = torch.randn(257, 64)
v = torch.randn(257, 64)
