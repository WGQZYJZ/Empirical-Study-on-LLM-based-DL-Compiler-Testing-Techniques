

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=None, inv_scale=1.0):
        super().__init__()
 
        self._dim = dim
        self._inv_scale  = torch.as_tensor(inv_scale)
 
    @staticmethod
    def compute_scaled_dot_product(q, k, v):
        scaled_dot_product  = q.matmul(k.transpose(-2, -1)) / q.shape[-1].sqrt()
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        return attention_weights.matmul(v), scaled_dot_product
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
 
        # Compute scaled dot product
        if self._inv_scale is not None and len(query.shape) > 2 and self._dim == tuple():
            self._dim = (1,) * ((len(key.shape) - 2)) + (-2, -1)

        scaled_dot_product, _  = self.compute_scaled_dot_product(query, key, value)
        return scaled_dot_product


# Initializing the model
scaled_dot_product_attention = ScaledDotProductAttention(dim=(-3, -2))

__output__  = scaled_dot_product_attention(query=torch.randn(16, 4, 8), key=torch.randn(16, 4, 8), value=torch.randn(16, 4, 8))

