
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=-1, scale=0):
        super().__init__()
        self.dim = dim
        self.scale = scale

    def forward(self, q, k, v, mask=None):
        