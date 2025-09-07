
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_module = torch.nn.MultiheadAttention(embed_dim=10, num_heads=5)
 
    def forward(self, query, key, value):
        qk = self.attention_module(query, key, value)
        return qk[0]


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(4, 10, 50, 32)
key   = torch.randn(4, 10, 60, 32)
value = torch.randn(4, 10, 60, 32)
