
class Model(torch.nn.Module):
    def __init__(self, key_dim, value_dim, d_model, num_heads):
        super().__init__()
        self.mha = torch.nn.MultiheadAttention(key_dim=key_dim, 
                                               output_dim=d_model, 
                                               num_heads=num_heads)
 
    def forward(self, query, key, value):
        attn  = self.mha(query, key, value)
        return attn
# Initializing the model
m = Model(key_dim=10, 
          value_dim=100, 
          d_model=200, 
          num_heads=3)


# Inputs to the model
query = torch.randn(5, 10, 64, 64) # (bsz * h * nhead, len_q, dim_kv)
key   = torch.randn(5, 20, 64, 64) # (bsz * h * nhead, len_k, dim_kv)
value = torch.randn(5, 20, 64, 64) # (bsz * h * nhead, len_v, dim_kv)


attn = m(query=query, key=key, value=value)
