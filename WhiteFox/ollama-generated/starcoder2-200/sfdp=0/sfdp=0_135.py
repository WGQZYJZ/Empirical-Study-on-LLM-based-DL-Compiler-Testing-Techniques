
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=0., **kwargs)
        super().__init__()
        self._inv_scale = torch.nn.Parameter(torch.tensor(inv_scale), requires_grad=False)
 
    @torch.jit.export
    def forward(self, query: Tensor, key: Tensor, value: Tensor):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self._inv_scale 
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


m  = ScaledDotProductAttention()


