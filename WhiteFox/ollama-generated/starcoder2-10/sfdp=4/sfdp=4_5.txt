
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask, value):
        v1 = torch.bmm(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        v2 = v1 + attn_mask  # Add the attention mask to the scaled dot product
        v3 = torch.softmax(v2, dim=-1)  # Apply softmax to the result
        v4 = torch.bmm(v3, value)  # Compute the dot product of the attention weights and the value tensor
        return v4

# Initializing the model