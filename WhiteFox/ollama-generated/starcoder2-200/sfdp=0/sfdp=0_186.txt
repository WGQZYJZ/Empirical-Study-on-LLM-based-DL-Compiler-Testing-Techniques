
class ScaledDotProductAttention(nn.Module):
    def __init__(self, inv_scale: float = 1.) -> None:
        super().__init__()
        self._inv_scale = inv_scale
 
    @property
    def _scale(self) -> int:
        return (self._inv_scale ** -2).sqrt()
 
    def forward(
            self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor,) -> Tuple[torch.Tensor]:
 
        scaled_dot_product = torch.matmul(query, key.transpose(-1, -2)) / self._scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights @ value  # [batch x heads x qlength x vlength]
 
        return output

# Initializing the model