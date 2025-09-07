
class Attention(nn.Module):
    def __init__(self):
        super().__init__()
        self.norm = nn.LayerNorm([4096])

    def forward(self, query, key, value, mask=None):
        qk  = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product 
        attn_weights  = torch.softmax(qk, dim=-1)  # Apply softmax to the result 
        output  = attn_weights @ value # Compute the dot product of the attention weights and the value
        return self.norm(output)

# Initializing the model
m = Attention()


# Inputs to the model