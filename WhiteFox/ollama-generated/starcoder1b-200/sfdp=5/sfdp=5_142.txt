
class Model(torch.nn.Module):
    def __init__(self, dim, num_heads, head_dim):
        super().__init__()

        self.self_attn = nn.MultiheadAttention(
            dim=dim,
            num_heads=num_heads,
            head_dim=head_dim)
 
        self.proj = nn.Linear(dim * 2, dim)
 
    def forward(self, x1, x2):
        x2q = self.self_attn(x1, x1, x1, attn_mask=x2)
        x2v = self.self_attn(x2, x2, x2, attn_mask=x2)

        # Compute the output of the transformer by applying the projection
        # layer after the self attention
        out = torch.matmul(torch.cat((x1, x2), dim=-1), self.proj.weight)
        return out


# Initializing the model
m = Model(dim=512, num_heads=8, head_dim=512)

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
x2 = torch.randn(10, 3, 64, 64)
