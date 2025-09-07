
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=None):
        super().__init__()
        self.inv_scale = inv_scale

    @staticmethod
    def _scaled_dot_product_attention(query, key, value, mask):
        