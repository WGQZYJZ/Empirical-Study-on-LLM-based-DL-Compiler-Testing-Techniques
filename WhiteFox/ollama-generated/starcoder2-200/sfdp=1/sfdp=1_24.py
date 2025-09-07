class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(embed_dim=256, num_heads=8)
 
    def forward(self, q1, k1, v1):
        v1, attn = self.attn(q1, k1, v1)
        return v1
