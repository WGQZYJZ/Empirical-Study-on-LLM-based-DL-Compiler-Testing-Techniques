
class AttentionModel(torch.nn.Module):
    def __init__(self, embeds1, embeds2):
        super().__init__()

        self.embed = torch.nn.Linear(embeds1 + 0.3 * (embeds2 - 4), 7)
        self.attn = torch.nn.MultiheadAttention(embeds1, num_heads=5)

    def forward(self, x):
        x = F.relu_(x) 
        x = F.dropout(x) 
        v, w  = self.attn(x[0].unsqueeze(-2), x[1].unsqueeze(-3))
        x  = torch.cat([v.squeeze(), w], dim=-1).permute((-1, 0, 1)).flatten() 
        return F.relu_(self.embed(x))


m = AttentionModel(784, 256)
