
class Model(torch.nn.Module):
    def __init__(self, num_heads = 8, **kwargs):
        super().__init__()
        self.attn_mask = torch.eye(8).view(1, -1, 8, 8)
        self.attn_dropout = torch.nn.Dropout(p=0.5, inplace=True)

        self.norm1 = torch.nn.LayerNorm(kwargs['dim'], eps=1e-3, elementwise_affine=False)

        self.attn1 = MultiheadAttention(**kwargs)
        self.norm2 = torch.nn.LayerNorm(kwargs['dim'], eps=1e-3, elementwise_affine=False)
        self.dropout = torch.nn.Dropout(p=0.5, inplace=True)

        self.norm3 = torch.nn.LayerNorm(kwargs['dim'], eps=1e-3, elementwise_affine=False)

        self.mlp1 = torch.nn.Sequential(
            torch.nn.Linear(kwargs['dim'] * 2, kwargs['dim']),
            torch.nn.GELU(),
            torch.nn.Dropout(0.5),
        )

    def forward(self, x1):
        k = self.norm1(x1)
        v = self.norm2(self.attn1(q=self.norm3(x1), k=k))

        h  = self.attn_dropout(h)
        output  = torch.matmul(h, v)  # (B, n, num_heads * dim) @ (B, n, num_heads * dim) -> (B, n, num_heads * dim)

        mlp1  = self.norm3(self.mlp1(torch.cat([output, x1], dim=2)))
        output  = self.dropout(output + mlp1)  # Add the intermediate outputs to the main output

        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
