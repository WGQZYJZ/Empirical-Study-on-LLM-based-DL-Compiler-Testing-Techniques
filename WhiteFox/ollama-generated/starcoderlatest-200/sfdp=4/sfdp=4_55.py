
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attn = torch.nn.MultiheadAttention(num_heads=8, embed_dim=512)
 
    def forward(self, x1, x2):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 512)
x2 = torch.randn(16, 3, 512)
