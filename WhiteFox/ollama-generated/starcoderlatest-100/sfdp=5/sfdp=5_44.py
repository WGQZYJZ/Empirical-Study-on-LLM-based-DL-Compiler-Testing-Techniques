
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=128):
        super().__init__()
        self.attn = torch.nn.Linear(hidden_dim * 2, hidden_dim)
        self.ffn = torch.nn.Sequential(
            torch.nn.Linear(hidden_dim * 2, hidden_dim),
            torch.nn.GELU(),
            torch.nn.Dropout(),
            torch.nn.Linear(hidden_dim, hidden_dim)
        )

    def forward(self, x1, x2):
        attn = self.attn(torch.cat([x1, x2], dim=-1))
        ffn = self.ffn(attn)
        return (attn + ffn).permute((0, 2, 3, 1))
