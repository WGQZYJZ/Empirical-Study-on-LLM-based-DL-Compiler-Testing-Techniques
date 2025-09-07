

class Attention(torch.nn.Module):
    def __init__(self, embed_dim=768, num_heads=12):
        super().__init__()

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        # Scaled dot product attention with key mask
        self.attn_scale  = torch.nn.Parameter(torch.ones(()), requires_grad=False)
        self.k_mask     = torch.zeros((1, embed_dim))

        # Scaled dot-product attention
        self.qk = torch.nn.Linear(embed_dim * 2, num_heads)
        self.v = torch.nn.Linear(embed_dim, num_heads)

    def forward(self, query: torch.Tensor, key: torch.Tensor):

        qkv = self.qk(query).chunk(3, dim=-1)
        value = self.v(*qkv)

        qk  = qkv[0] @ qkv[2].transpose(-2, -1) / math.sqrt(self.head_dim) + self.attn_scale * torch.masked_fill(self.k_mask, float('-inf'), 0.)
        attn_weight = torch.softmax(qk, dim=-1)

        return attn_weight @ value


m  = Attention()

input_query  = torch.randn(32, 768)
input_key   = torch.randn(32, 768)

out          = m(input_query, input_key)

print(f'{out.shape}')

