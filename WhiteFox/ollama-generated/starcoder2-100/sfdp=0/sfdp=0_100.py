
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=100., **kwargs) -> None:
        super().__init__()
 
        self._inv_scale = inv_scale
 
    def forward(self, query, key, value):
        # Apply scaling factor
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.shape[-1]) * self._inv_scale
 
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Initializing the model