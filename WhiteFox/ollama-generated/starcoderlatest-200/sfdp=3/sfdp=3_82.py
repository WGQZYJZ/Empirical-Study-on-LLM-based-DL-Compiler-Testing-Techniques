
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, value)[0]
        return qk

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 8, 32, 64)
key   = torch.randn(1, 8, 32, 64)
value = torch.randn(1, 8, 32, 64)
