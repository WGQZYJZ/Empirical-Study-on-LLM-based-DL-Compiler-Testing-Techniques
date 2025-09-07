
class Model(torch.nn.Module):
    def __init__(self, d_model=64, nhead=8):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead

        assert d_model % nhead == 0
        self.d_inner = d_model // nhead

        # Multi-head attention mechanism: (batch_size, n_query, n_key, head_dim) -> (batch_size, n_query, n_attn_heads, n_k_len * n_v_len)
        self.attn = torch.nn.MultiheadAttention(d_model=d_model, num_heads=nhead)
 
    def forward(self, x1, query, key):
        # Multi-head attention mechanism: (batch_size, n_query, n_key, head_dim) -> (batch_size, n_query, n_attn_heads, n_k_len * n_v_len)
        attn  = self.attn(x1, query, key)[0] # [64 x 65]

        # Apply dropout after computing the dot product of the attention output and the value tensor: (batch_size, n_query, n_attn_heads, n_k_len * n_v_len)
        attn = torch.nn.functional.dropout(attn, p=0.5) # [64 x 65]

        # Compute the dot product of the attention output and the value tensor: (batch_size, n_query, n_attn_heads, n_v_len)
        out  = attn.matmul(x1) # [64 x 65 x 8]
        
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 8, 64, 64)
query = torch.randn(32, 8, 64, 512)
key = torch.randn(32, 8, 512, 512)
