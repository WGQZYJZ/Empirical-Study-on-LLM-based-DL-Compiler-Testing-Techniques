
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(32, 8)
 
    def forward(self, query, key=None, value=None):
        v1  = self.attn(query, key, value) 
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
query_0 = torch.randn(2, 64, 32)
key_0 = query_0  # If key is None it will compute key as query and then value from query and key
value_0 = key_0

