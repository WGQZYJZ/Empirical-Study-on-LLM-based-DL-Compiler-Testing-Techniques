
class ScaledDotProductAttention(nn.Module):
    def __init__(self, d_k, scale=1.0, bias=False):
        super().__init__()
        self.d_k = d_k
        self.scale = scale
        self.bias = bias

    @staticmethod
    def _batch_matmul(x, y):
        