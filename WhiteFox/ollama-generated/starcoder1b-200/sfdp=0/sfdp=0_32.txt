
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=-1, eps=1e-6):
        super().__init__()
        self.dim = dim
        self.eps  = eps

    def forward(self, q, k, v):
        attn = torch.matmul(q, k) / (sqrt(k.size(-1)) * sqrt(v.size(-1)))
        scale  = torch.rsqrt((attn + self.eps).clamp(min=self.eps)).unsqueeze(-1)
        return q * scale


# Initializing the model
m  = ScaledDotProductAttention()

 # Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
k1 = torch.randn(3, 8, 5, 5)
v1 = torch.randn(3, 8, 5, 5)
