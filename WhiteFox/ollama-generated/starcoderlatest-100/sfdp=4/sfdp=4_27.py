
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2) / math.sqrt(x1.size(-1))  # Compute the dot product of the query and key, and scale it
        v1 = v1 + attn_mask  # Add the attention mask to the scaled dot product
        v2 = torch.softmax(v1, dim=-1)  # Apply softmax to the result
        output = torch.matmul(v2, x2)  # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
attn_mask = torch.eye(attn_weights.size(-1)) * -1e4  # Use negative infinity as a masking value for attention weights
attn_m = Attention(attn_weights.size(-1))
query = torch.randn(6, dim)
key = torch.randn(6, dim)
v1 = attn_m(query, key)

