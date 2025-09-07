
class Attention_DotProduct(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
a_d = Attention_DotProduct()

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)
