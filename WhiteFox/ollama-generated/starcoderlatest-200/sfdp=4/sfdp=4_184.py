
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=1, key_dim=2)
 
    def forward(self, query, key, value, attn_mask):
        # Compute the dot product of the query and key, and scale it
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))  # (B, Lq, Lk) @ (Bk, Dk, Dv) -> (B, Lq, Lk)
        qk = qk + attn_mask  # (B, Lq, Lk) + (B, Lm, Lm) -> (B, Lq, Lk)
        attn_weight = torch.softmax(qk, dim=-1)  # (B, Lq, Lk)
        output = torch.matmul(attn_weight, value)  # (B, Lq, Dv) @ (B, Lm, Dv) -> (B, Lq, Dv)
        return output
