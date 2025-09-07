
class MultiHeadAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        k = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
 
        if not (attn_mask is None):
            k  += attn_mask
    
        weight  = torch.softmax(k, dim=-1) 
        output = weight @ value
        
        return output


# Initializing the model