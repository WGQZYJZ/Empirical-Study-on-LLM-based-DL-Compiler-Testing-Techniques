
class Model(torch.nn.Module):
    def __init__(self, n_head = 8, dim = 64):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim, n_head)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + 1 # Add one to the result of scaling
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = self.attn(attn_weight, value, value)[0] # Compute attention weighted sum between query and value (attention weights are already applied in this line)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
