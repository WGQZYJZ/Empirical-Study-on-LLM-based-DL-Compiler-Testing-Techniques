
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=128, num_heads=4):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            embed_dim = embedding_dim,
            num_heads = num_heads)
 
    def forward(self, query, key, value):
        qk  = self.attn(query, key, value)[0] # Apply the attention mechanism
        return qk
# Initializing the model
m = Model()
# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(1, 2, 64, 64)
value = torch.randn(1, 2, 64, 64)
