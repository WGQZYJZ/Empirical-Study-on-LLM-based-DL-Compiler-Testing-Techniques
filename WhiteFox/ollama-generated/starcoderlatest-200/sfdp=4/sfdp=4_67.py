
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weights = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weights @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(5, 8, 10, 16)
key = torch.randn(8, 8, 10, 16)
value = torch.randn(8, 8, 20, 32)
attn_mask = torch.eye(16).unsqueeze(dim=0)
