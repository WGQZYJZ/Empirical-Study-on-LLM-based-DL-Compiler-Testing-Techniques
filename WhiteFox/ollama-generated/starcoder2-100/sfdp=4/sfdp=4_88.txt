
class MultiHeadAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        # Scaled dot-product attention
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        if attn_mask is not None:
            qk += attn_mask
 
        # Compute the attention weights
        attn_weight  = torch.softmax(qk, dim=-1)
 
        
        output  = attn_weight @ value
       
        return output

# Initializing model
m = MultiHeadAttention()


# Inputs to the model
query  = torch.randn(8, 32, 64)
key   = query + 1
value = key * 0.5
attn_mask = None
