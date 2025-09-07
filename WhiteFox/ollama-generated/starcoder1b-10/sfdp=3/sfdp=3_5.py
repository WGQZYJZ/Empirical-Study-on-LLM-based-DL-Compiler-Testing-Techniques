
class Model(torch.nn.Module):
    def __init__(self, d_k, heads=8, scale_factor=1.0):
        super().__init__()
        self.scale = torch.sqrt(d_k)
        self.d_k = d_k
        self.heads = heads
        self.attn = MultiHeadAttention(
            d_k, heads, scale=scale_factor
        )
        self.proj = torch.nn.Linear(
            d_k, d_v * heads, bias=False
        )
 
    def forward(self, x1, x2):
        key, value = self.attn(x1, x2)
        return self.proj(dropout(value))


# Initializing the model
m  = Model()


# Inputs to the model
d_k = __output__.size(-1)
x1  = torch.randn(1, 3, 64, 64)
