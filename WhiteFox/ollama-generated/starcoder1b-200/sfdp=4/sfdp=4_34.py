
class Model(torch.nn.Module):
    def __init__(self, d_k, nhead=8, dim=-1):
        super().__init__()
        self.wte = torch.nn.Linear(d_k * 2, d_k)
        self.wpe = torch.nn.Linear(d_k, d_k * 2)
        self.layer_norm = torch.nn.LayerNorm(d_k)
 
        self.self_attn = torch.nn.MultiheadAttention(nhead=nhead, dim=dim)
 
    def forward(self, x1):
        # (batch, seq_len_q, d_k) -> (batch, seq_len_q, seq_len_k)
        q1  = self.wpe(x1).transpose(-2, -1)  # Compute the query layer-by-layer (the 'query' matrix) and scale it
        k1  = self.wte(x1).transpose(-2, -1)
        q1 = self.layer_norm(q1)
 
        # (batch, seq_len_k, seq_len_k) -> (batch, seq_len_q, seq_len_k)
        k2  = self.wpe(x1).transpose(-2, -1)  # Compute the key layer-by-layer and scale it
        v1  = self.wte(x1).transpose(-2, -1)
        v1 = self.layer_norm(v1)
 
        q2  = self.self_attn(q1, k2, value=v1) # Compute the output of a multi-head attention layer
        out = q2.contiguous().view(x1.shape[0], x1.shape[1], -1).transpose(-2, -1)  # (batch, seq_len_q, dim) -> (batch, seq_len_q, dim, d_k)
 
        return out
 

# Initializing the model
m = Model(d_k=5)


