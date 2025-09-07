
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_weights = torch.nn.Parameter(torch.zeros(1, 8, 64, 64))
 
    def forward(self, query, key):
        v2 = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        v3 = torch.softmax(v2 + self.attn_weights, dim=-1)  # Apply softmax to the scaled dot product
        v4 = v3 @ value  # Compute the dot product of the attention weights and the value
        return v4

# Inputs to the model
query = torch.randn(1, 8, 64, 64)
key = torch.randn(1, 8, 64, 64)
