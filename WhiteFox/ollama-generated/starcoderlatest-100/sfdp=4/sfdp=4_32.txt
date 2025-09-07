
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 128)
 
    def forward(self, query, key, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(2, 3, 64, 64)
key    = torch.randn(1, 3, 64, 64)
attn_mask = torch.ones((2, 1), dtype=torch.int8, device='cpu') # The attention mask must be of size (batch, 1). Note the dtype must be int8, and device is cpu


