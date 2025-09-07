
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 8, 32, 40)
key   = torch.randn(16, 4, 32, 40)
value = torch.randn(16, 8, 32, 40)
attn_mask = torch.zeros(16, 1, 32, 40).to(query)
