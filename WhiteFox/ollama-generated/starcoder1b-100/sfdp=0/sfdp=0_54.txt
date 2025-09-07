
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tuple[Tensor, Tensor]:
        # (b1, t1, d1, h1, w1) * (b2, t2, d2, h2, w2) -> (b1, t1, b2, t2, d1 + d2, h1 + h2)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.div(key.shape[-1], key.shape[0]))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        return attention_weights.matmul(value), None


# Initializing the model
m  = ScaledDotProductAttention()


