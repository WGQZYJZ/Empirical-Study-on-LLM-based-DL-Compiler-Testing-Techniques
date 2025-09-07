
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, query_dim=64, key_dim=128, value_dim=64):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=num_heads, key_dim=key_dim, value_dim=value_dim)

    def forward(self, qk, v):
        attn_weight, _ = self.attn(qk, qk, qk)  # Apply attention mechanism on queries and keys
        output = attn_weight @ v
        return output

# Initializing the model
m = Model()


