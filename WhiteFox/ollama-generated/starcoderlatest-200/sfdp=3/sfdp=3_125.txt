
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads=num_heads)

    def forward(self, query, key, value, mask=None):
        if mask is not None:
            assert len(mask.shape) == 3 and mask.shape[0] == 1
        qk, attn = self.attn(query, key, key, mask=mask) # Calculate the attention
        return qk


# Initializing the model
m = MultiHeadAttention(64)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
mask = None # Applying mask if exists
