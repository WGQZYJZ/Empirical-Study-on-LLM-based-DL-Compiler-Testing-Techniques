
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, dim, num_heads=8):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(query_dim=query_dim,
                                              key_dim=key_dim,
                                              num_heads=num_heads)
        self.linear = torch.nn.Linear(query_dim * num_heads, dim)
 
    def forward(self, query, value):
        # Query and key are (B, S1, C), where C is the size of each head in transformer layers
        attn_weights = self.attn(query, key=value, value=value)[0]
        return self.linear(attn_weights)


# Initializing the model
m = Model(32, 64, 128)

# Inputs to the model
q1, k1, v1 = torch.randn(16, 5, 32), torch.randn(16, 10, 64), torch.randn(16, 10, 128)
