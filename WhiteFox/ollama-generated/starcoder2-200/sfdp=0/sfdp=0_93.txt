
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=-1) -> None:
        super().__init__()
        self._dim  = dim
        self._inv_scale  = torch.rsqrt(torch.tensor([2048], dtype=torch.float32))
 
    @staticmethod
    def scaled_dot_product_attention(query, key, value):
        scaled_dot_product  = query @ key.transpose(-2, -1) / self._inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        return attention_weights @ value
 
    def forward(self, query, key, value):
        attention_weights  = ScaledDotProductAttention.__scaled_dot_product_attention__(query, key, value)
