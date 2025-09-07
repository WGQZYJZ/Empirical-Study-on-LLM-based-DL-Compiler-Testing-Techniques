
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale: float = 1., **kwargs):
        super().__init__()

        self.query = torch.nn.Parameter(torch.randn(32))
        self.key   = torch.nn.Parameter(torch.randn(32))
        self.value = torch.nn.Parameter(torch.randn(32))

        self._scale = inv_scale

    def forward(self, **kwargs):
        scaled_dot_product  = torch.matmul(query, key.transpose(-1, -1)) / sqrt(d) # d is the dimension of the key/query vectors
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output             = attention_weights.matmul(value)
        return output
