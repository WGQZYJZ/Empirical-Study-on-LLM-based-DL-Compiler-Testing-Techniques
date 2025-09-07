
class Model(torch.nn.Module):
    def __init__(self, embed_dim=128, num_heads=8, dim=768, depth=4, heads=8):
        super().__init__()
        self.head = torch.nn.MultiheadAttention(embed_dim, num_heads)
        self.ln1 = torch.nn.LayerNorm(dim)
        self.ln2 = torch.nn.LayerNorm(dim)
        self.fc = torch.nn.Linear(dim * heads, dim)
 
    def forward(self, x):
        q = self.head(x, x, x)[0]  # [B, L, T, N]
        k = self.head(x, x, x)[1]  # [B, L, T, N]
        attn_weight = torch.softmax(q @ k, dim=-1)  # [B, L, T, H]
        output = attn_weight @ x
        output = self.ln2(output + self.fc(self.head(x, x, x)[0]))
        return output


# Initializing the model
m = Model()


