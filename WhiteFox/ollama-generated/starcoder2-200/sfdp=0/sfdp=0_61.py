
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale: float = 1., **kwargs) -> None:
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights   = scaled_dot_product.softmax(dim=-1)
        output              = attention_weights.matmul(value)
 
        return output
