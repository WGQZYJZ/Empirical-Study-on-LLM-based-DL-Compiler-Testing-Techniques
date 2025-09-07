
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv  = torch.nn.Linear(768, 3 * 4)
        self.norm_q = nn.LayerNorm(3 * 4)
        self.scale = (math.pow(10000, -5)) ** (-0.5)

    def forward(self, x1):
        qkv = self.qkv(x1).chunk(3, dim=1)  # Chunk the input feature dimension by batch and channel into two vectors: b1, c1, ..., bn, cn
        q  = qkv[0] * self.scale  # Apply layer normalization to both the query and key components
        k  = qkv[1] * self.scale
        v  = qkv[2] * self.scale

        q_normalized = self.norm_q(q)
        k_normalized = self.norm_q(k)
        v_normalized = self.norm_q(v)

        scale = torch.sqrt(torch.sum(q ** 2, dim=-1, keepdim=True))
        inv_scale = 1.0 / scale
        attention_weights = (q_normalized @ k_normalized) * inv_scale

        output = attention_weights @ v_normalized
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
