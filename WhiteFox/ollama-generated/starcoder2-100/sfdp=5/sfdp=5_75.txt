
class Attention(torch.nn.Module):
    def __init__(self, d_model=768):
        super().__init__()
 
    def forward(self, query, key, value): 
        attn  = (query @ key.transpose(-2, -1)) / math.sqrt(key.size(-1)) # Dot product of the query and key with sqrt scaling
        attn += self._mask()  # Add an attention mask to it
        
        attn_w = torch.softmax(attn, dim=-1) # Apply softmax on the result
        attn_w = torch.dropout(attn_w, p=0.85, training=True) # Apply dropout
        out = (attn_w @ value)  # Dot product of the attention weight and values
        return out


# Initializing model
attn  = Attention()
 
# Inputs to the model
key  = torch.randn(32, 64, 1024).to('cuda')
value  = torch.randn(32, 8, 512).to('cuda')
qry  = torch.randn(32, 8, 768).to('cuda')
 
# Masking 
attn._mask() 
 
