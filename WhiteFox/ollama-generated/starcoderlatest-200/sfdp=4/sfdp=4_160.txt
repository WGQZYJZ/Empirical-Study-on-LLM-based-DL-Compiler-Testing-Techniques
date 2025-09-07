
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention(num_heads=4,
                                                          embed_dim=64)
 
    def forward(self, query, key, value, attn_mask):
        v, attn_weights = self.attn_layer(query, key, value, attn_mask) # Compute scaled dot-product attention weights
        output = torch.matmul(attn_weights, value)  # Compute the weighted sum of the values
        return output


# Inputs to the model
query  = torch.randn(8, 4, 64, 64)  # shape: (batch_size * num_heads, seq_len, dim)
key    = torch.randn(10, 2, 64, 64) # shape: (batch_size * num_heads, num_attention_heads, seq_len, seq_len)
value  = torch.randn(8, 2, 64, 64)  # shape: (batch_size * num_heads, num_attention_heads, seq_len, seq_len)
attn_mask = torch.ones(10, 4, 64, 64)  # shape: (batch_size, num_heads, seq_len, seq_len)
