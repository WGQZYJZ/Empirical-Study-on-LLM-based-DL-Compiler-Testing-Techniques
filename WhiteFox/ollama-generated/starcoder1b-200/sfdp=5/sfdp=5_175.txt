
class Model(torch.nn.Module):
    def __init__(self, qkv_size=16384, dim=512):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm(dim)

        # The first layer of the transformer
        self.scale  = nn.Parameter(torch.zeros(qkv_size))
        self.shift = nn.Parameter(torch.zeros(qkv_size))
        self.q = torch.nn.Linear(dim, qkv_size // 2)

        # The second layer of the transformer
        self.k = torch.nn.Linear(dim, qkv_size // 2)

        # The third layer of the transformer
        self.v = torch.nn.Linear(dim, qkv_size // 2)

    def forward(self, x):
        # Compute query
        q = self.q(x)  # B C H W QK
        k = self.k(x)  # B C H W KQ
        v = self.v(x)  # B C H W VQ

        # Compute the attention weights between q and k
        attn_weight = torch.matmul(q, k.transpose(-2, -1))  # B C KH W (QK * KH) / sqrt(K)
        # Multiply by sqrt(KH), so that the final values range in [0, 1]
        attn_weight /= math.sqrt(k.size(-1))

        # Compute value
        value = torch.matmul(attn_weight, v)  # B C KW VQ

        # Add scaling and shifting to the output
        out = self.layer_norm(x + self.shift.unsqueeze(-2).unsqueeze(-1) @ attn_weight.unsqueeze(-1)
                             + self.scale.unsqueeze(-2).unsqueeze(-1) * value)  # B C H W (SQ * VQ) + O

        return out

# Initializing the model
m = Model()
x1 = torch.randn(1, 512, 64, 64)
