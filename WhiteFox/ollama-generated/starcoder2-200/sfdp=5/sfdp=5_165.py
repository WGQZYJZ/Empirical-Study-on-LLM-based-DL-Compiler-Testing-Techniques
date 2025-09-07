
class SelfAttentionBlock(torch.nn.Module):
    def __init__(self, qk_dim):
        super().__init__()
        self.attn = torch.nn.Linear(qk_dim * 2 + qk_dim, qk_dim)
 
    def forward(self, query, key, value, attn_mask=None):
        v1  = (query @ key.transpose(-2,-1)) / math.sqrt(query.size(-1)) 
        if self._use_attn_mask:
            v1 += attn_mask
        v2  = torch.softmax(v1, dim=-1) # Apply softmax to the scaled dot product of query and key
        v3  = torch.dropout(v2, dropout_p, True) # Apply dropout to the softmax output 
        