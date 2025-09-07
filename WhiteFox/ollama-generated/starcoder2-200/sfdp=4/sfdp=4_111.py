
class DotProductAttention(torch.nn.Module):
    def __init__(self, d_model, attn_mask=None):
        super().__init__()
 
        # Compute the dot product of the query and key, and scale it
        self.attn = torch.nn.Linear(d_model * 2, d_model)
 
        if attn_mask is not None:
            # Add the attention mask to the scaled dot product
            self.attn_mask = attn_mask
 
    def forward(self, query, key):
        
        v1  = key.transpose(-2, -1)
        v2  = torch.matmul(query, v1)
        v3  = v2 / math.sqrt(query.size(-1))
        if hasattr(self, 'attn_mask') and self.attn_mask is not None:
            attn_weight  = (v3 + self.attn_mask).masked_fill_(v3 == float('-inf'), 0.)
            attn_weight = torch.softmax(attn_weight, dim=-1)
            v4  = v2 @ value
        else: 
            v5  = F.softmax(v3, -1)
            v6  = v1 @ key
            v7  = v6 / math.sqrt(key.size(-1))

        return output