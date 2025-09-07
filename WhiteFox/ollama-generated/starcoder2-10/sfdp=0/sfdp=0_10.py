
class DotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale = 1024 ** -0.5):
        super().__init__()
 
        self.scale  = 1 / inv_scale
        self._qkv_proj  = torch.nn.Linear(384, 96)
        self._o_proj  = torch.nn.Linear(96, 72)
 
    def forward(self, query, key, value):
            qk = torch.cat([query] * 10 + [key], dim=-1).reshape(-1, 384 + 384)
            vq  = self._qkv_proj(qk)
            vs  = self._o_proj(vq)
            scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
            attention_weights  = scaled_dot_product.softmax(dim=-1).reshape(query.shape[0], query.shape[-2] * 384 + 96)
            output  = attention_weights.matmul(value)
            return output


# Initializing the model with inv_scale of `inv_scale`
m = DotProductAttention(15752 ** -0.5)

# Inputs to the model
query  = torch.randn(1, 384, 6) # Query tensor
key  = torch.randn(96, 384, 1) # Key tensor
value  = torch.randn(96, 72, 10) # Value tensor


