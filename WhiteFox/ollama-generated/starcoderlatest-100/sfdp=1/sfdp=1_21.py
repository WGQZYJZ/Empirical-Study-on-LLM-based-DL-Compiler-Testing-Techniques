
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.linear_qk = torch.nn.Linear(
            in_features=embed_dim * 3, out_features=embed_dim * 4)
        self.linear_v = torch.nn.Linear(in_features=embed_dim * 4,
                                      out_features=embed_dim * 2)
 
    def forward(self, qk_input):
        q_ = qk_input[:, :, :self.embed_dim]
        k_ = qk_input[:, :, self.embed_dim:self.embed_dim * 2]
        v_ = qk_input[:, :, -self.embed_dim:]
        q_ = torch.transpose(q_, -1, -2)
        # Linear projections of query, key, and value for each head
        # Concatenate all heads at once (B x n_heads x L x H)
        h = self.linear_qk(
            torch.cat([torch.unsqueeze(q_, dim=-3),
                       torch.unsqueeze(k_, dim=-3),
                       torch.unsqueeze(v_, dim=-3)], dim=-2))
        # Apply linear projection and split into heads (B x n_heads x L x 4H)
        h = torch.transpose(h, -1, -2)
        output = self.linear_v(h)
 
        return output
# Initializing the model
m = MultiHeadSelfAttention(embed_dim=64, num_heads=8)

 # Inputs to the model
qk_input = torch.randn(1, 3, 64, 64 * 4)
