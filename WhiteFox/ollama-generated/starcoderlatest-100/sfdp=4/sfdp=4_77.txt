
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(1, 8, dropout=0.2)
 
    def forward(self, q1, k1, v1, attn_mask=None):
        output, _ = self.attn(q1, k1, v1, attn_mask=attn_mask)
        return output


# Inputs to the model
query  = torch.randn(4, 8, 64, 64) # Query tensor with shape (batch size * num heads * head dimension * query length)
key    = torch.randn(12, 8, 64, 64) # Key tensor with shape (batch size * num heads * head dimension * key length)
value  = torch.randn(36, 8, 64, 64) # Value tensor with shape (batch size * num heads * head dimension * value length)
attn_mask  = torch.ones((12,), dtype=torch.int64) # Attention mask tensor with shape (num attention heads,)


# Output of the model
output = m(query, key, value, attn_mask)


