
class Model(torch.nn.Module):
    def __init__(self, num_heads=1, num_blocks=2):
        super().__init__()
        self.num_heads = num_heads  # Number of heads in this model
        self.num_blocks = num_blocks  # Number of blocks in this model
        self.dim = num_heads * dim // 8
        self.layer = torch.nn.ModuleList([self.TransformerEncoderLayer(dim) for _ in range(num_blocks)])
 
    def forward(self, x):
        h = x
        for layer in self.layer:
            h = layer(h)
        return h
 
    # Transformer Encoder Layer
    class TransformerEncoderLayer(torch.nn.Module):
        def __init__(self, dim=128, ff_dim=4096):
            super().__init__()
            self.self_attn = torch.nn.MultiheadAttention(dim, num_heads)
            self.pos_emb = torch.nn.Parameter(torch.randn((1, 1, x.shape[-2], x.shape[-1])) * 0.005)
            self.feed_forward = torch.nn.Linear(ff_dim, ff_dim // 4)

        def forward(self, x):
            query = torch.matmul(x, self.pos_emb)
            key = torch.transpose(x, 1, 2).contiguous()
            value = torch.transpose(x, 1, 2).contiguous()
            qkv = torch.cat([query, key, value], dim=-2)
            attn_weights = self.self_attn(qkv)
            context = self.self_attn(qkv, x=context)
            out_p = self.feed_forward(context.matmul(attention)) + query
            return torch.nn.functional.gelu(out_p)


# Initializing the model
m = Model()


