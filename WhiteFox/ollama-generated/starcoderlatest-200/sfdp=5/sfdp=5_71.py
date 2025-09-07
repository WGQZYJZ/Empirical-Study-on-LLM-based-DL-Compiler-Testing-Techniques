
class Model(torch.nn.Module):
    def __init__(self, query_dim=512, key_dim=64, value_dim=256, num_heads=2):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(query_dim, key_dim, num_heads)
 
    def forward(self, q, k, v):
        qk  = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_weight  = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = self.attention(attn_weight, v)[0]  # Get the attention output
        return output


# Initializing the model
m = Model()
q1 = torch.randn(4, 512, 16, 16)
k1 = torch.randn(32, 512, 8, 8)
v1 = torch.randn(4, 256, 16, 16)
