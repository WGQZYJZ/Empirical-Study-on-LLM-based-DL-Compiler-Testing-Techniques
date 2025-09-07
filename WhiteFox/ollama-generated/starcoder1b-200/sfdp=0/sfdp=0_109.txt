
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=-1, inv_sqrt_scale=None, eps=1e-7):
        super().__init__()
        self.dim = dim
        self.eps = eps
        if not isinstance(inv_sqrt_scale, float) and inv_sqrt_scale is not None:
            raise ValueError("Inv square root scale should be a scalar or None.")
        self.inv_sqrt_scale = inv_sqrt_scale

    def forward(self, x1, x2):
        inv_sqrt_scale = self.inv_sqrt_scale if self.inv_sqrt_scale is not None else self.eps ** 0.5
        return torch.matmul(x1, x2).div_(inv_sqrt_scale)


# Initializing the model
attn = ScaledDotProductAttention()


