
class Model(torch.nn.Module):
    def __init__(self, dim_qk=64, dim_key=128, d_model=512, nhead=8):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim_qk, dim_key, num_heads=nhead)
 
    def forward(self, query, key, value, attn_mask):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = self.attn(attn_weight, value, value)[0] # Compute the weighted sum of the value and the key
        return output


# Initializing the model
m = Model()

# Inputs to the model
qkv  = torch.randn(128, 512, 3)
