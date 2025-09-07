
class Model(torch.nn.Module):
    def __init__(self, n_head=1, n_dim=32, max_len_q=50, max_len_kv=768):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(n_head=n_head, d_k=n_dim, d_v=n_dim)
        self.proj_q = torch.nn.Linear(max_len_q*n_dim, max_len_kv)
        self.proj_k = torch.nn.Linear(max_len_kv*n_head, max_len_kv)
        self.proj_v = torch.nn.Linear(max_len_kv*n_head, max_len_kv)
 
    def forward(self, q1, k1):
        # Attention layer
        attn_out, attn_weight = self.attn(q1, k1, v=None)
 
        # Fully-connected projections
        q2 = torch.nn.functional.dropout(attn_out, dropout_p, training=True)
        q3 = self.proj_q(q2.reshape(-1, self.n_dim)).transpose(-2, -1).contiguous()
        k2 = torch.nn.functional.dropout(k1, dropout_p, training=True)
        k3 = self.proj_k(k2.reshape(-1, n_head*self.n_dim)).transpose(-2, -1).contiguous()
        v2 = torch.nn.functional.dropout(attn_weight, dropout_p, training=True)
        v3 = self.proj_v(v2.reshape(-1, n_head*self.n_dim)).transpose(-2, -1).contiguous()
 
        # Combine heads
        return q3 + k3 + v3


# Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(16, 10, 5)
k1 = torch.randn(16, 8, 470)
