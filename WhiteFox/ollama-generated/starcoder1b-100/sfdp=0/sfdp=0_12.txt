
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, query, key, value):
        # The implementation is just a copy-paste from previous chapter.
        ...

    def compute_scaled_dot_product_attention(self, q: Tensor, k: Tensor, v: Tensor, squeeze=True) -> Tensor:
        