
class Model(torch.nn.Module):
    def __init__(self, k1: int = 32, k2: int = 32, n_heads=8, dropout_p=0.5) -> None:
        super().__init__()

        self.k1 = torch.nn.Linear(in_features=4, out_features=k1)
        self.norm = torch.nn.LayerNorm([k1])
        self.attn1 = torch.nn.MultiheadAttention(
            embed_dim  = k2, num_heads = n_heads
        )

        self.k2 = torch.nn.Linear(in_features=4 + k2, out_features=k2)
        self.norm2 = torch.nn.LayerNorm([k2])
        self.attn2 = torch.nn.MultiheadAttention(
            embed_dim  = k1, num_heads = n_heads
        )

    def forward(self, x):

        v1 = self.k1(x)
        v1 = self.norm(v1)

        v1, v2 = self.attn1(v1, v1)[0]
        v3 = torch.cat([x, v1], 1)
        v4 = self.norm2(self.k2(v3))

        v5, v6 = self.attn2(v4, v4)[0]

        return (v5 + x).div_(4), v6

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(32, 4)

