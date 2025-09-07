
class Model(torch.nn.Module):
    def __init__(self, hidden_size: int, num_heads: int):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(hidden_size, num_heads)
 
    def forward(self, x1, q, k, v):
        v1  = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)) # Compute the dot product of the query and key, and scale it
        v2, attn_weight = self.attn(v1, q, k, v) # Apply multi-head attention to the output of the previous step
        v3  = v2 + v  # Add the output of the first step (i.e., the attention weights) and the value
        return v3


# Initializing the model
m = Model(hidden_size=16, num_heads=4)

# Inputs to the model
q = torch.randn(8, 8, 16, 16) # The first dimension is batch size (1 here), while the second two dimensions are sequence length and feature dim
k = torch.randn(8, 32, 16, 16)
v = torch.randn(8, 32, 16, 16)
