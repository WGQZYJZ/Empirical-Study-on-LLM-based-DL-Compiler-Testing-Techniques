
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.attn_projection = torch.nn.Linear(hidden_size * 2, hidden_size)
        self.value_projection = torch.nn.Linear(hidden_size * 2, hidden_size)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
        return self.attn_projection(torch.cat([query, key], dim=-1))


# Initializing the model
m = Model(hidden_size=8)

# Inputs to the model
q = torch.randn(2, 3, 64, 64)
k = torch.randn(2, 3, 64, 64)
v = torch.randn(2, 3, 64, 64)
