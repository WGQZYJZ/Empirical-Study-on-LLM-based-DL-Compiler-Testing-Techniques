
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=1e-6):
        super().__init__()
        self._inv_scale = 1 / math.sqrt(inv_scale)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> Tuple[torch.Tensor]:
 
        scaled_dot_product  = (query * key).sum(-2)
        attention_weights  = F.softmax(scaled_dot_product / self._inv_scale)
        output = attention_weights @ value
        return output
