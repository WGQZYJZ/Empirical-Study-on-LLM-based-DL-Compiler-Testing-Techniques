
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attn = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, query, key, value, attn_mask=None):
        # Compute the dot product of the query and key, and scale it
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) 
        # Add the attention mask to the scaled dot product
        if attn_mask is not None:
            qk += attn_mask
 
        # Apply softmax to the result
        attn_weight = torch.softmax(qk, dim=-1)
 
        # Compute the dot product of the attention weights and the value
        output = attn_weight @ value
 
        return output


# Inputs to the model
query  = torch.randn(4, 512, 64, 64)
key = torch.randn(4, 512, 64, 64)
value = torch.randn(4, 512, 64, 64)
attn_mask  = None
