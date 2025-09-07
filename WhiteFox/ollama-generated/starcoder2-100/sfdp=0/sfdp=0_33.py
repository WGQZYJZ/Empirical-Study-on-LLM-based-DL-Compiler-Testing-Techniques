
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=1., eps=None):
        super().__init__()
        self.eps = eps or 0.001

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        assert len(query.shape[:-2]) == 1 and len(key.shape[:-2]) == 1 \
               and len(value.shape[:-2]) == 1 \
               or query.shape[-3] == key.shape[-3] == value.shape[-3],\
            'Invalid inputs, shapes: %s %s %s' %(query.shape[:-2], key.shape[:-2], value.shape[:-2])
        inv_scale = float(inv_scale)

        scaled_dot_product  = torch.matmul(query, key.transpose(-1, -2)) / math.sqrt(key.size(-3), dtype=torch.float64) 
        if self.eps is not None:
            scaled_dot_product = torch.clamp(scaled_dot_product, min=-self.eps, max=self.eps)
        attention_weights  = scaled_dot_product.softmax(dim=-1)

        return attention_weights.matmul(value), attention_weights

# Initializing the model
m  = ScaledDotProductAttention()

