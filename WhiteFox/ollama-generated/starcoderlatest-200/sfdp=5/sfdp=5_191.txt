
class Model(torch.nn.Module):
    def __init__(self, embed_dim=512, num_heads=8, attn_dropout=0., relu_dropout=0.):
        super().__init__()
        self.attn_drop = nn.Dropout(attn_dropout)
        self.proj_q = nn.Linear(embed_dim, embed_dim, bias=False)
        self.attn_layer_norm = nn.LayerNorm(embed_dim)
 
        num_attention_heads = num_heads
        attention_head_size = int(embed_dim / num_attention_heads)
        self.all_head_layers = nn.ModuleList([nn.Linear(embed_dim, num_attention_heads * attention_head_size) for _ in range(num_attention_heads)])
        self.proj_k = nn.Linear(embed_dim, embed_dim, bias=False)
        self.proj_v = nn.Linear(embed_dim, embed_dim, bias=False)
 
        self.attn_layer_norm2 = nn.LayerNorm(embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)
 
    def forward(self, x1):
        q = self.attn_drop(self.proj_q(x1))
 
        qk = torch.einsum('bnqd,bnkd->bnqk', [q, k]) / math.sqrt(q.size(-1))  # compute the dot product
        attn_mask = torch.ones_like(qk).triu_(diagonal=1)
        attn_mask = attn_mask.float()

        qk += attn_mask
        attn_weights = nn.Softmax(dim=-1)(qk)
        attn_weights = self.attn_drop(attn_weights)
 
        x2 = torch.einsum('bnqd,bnqk->bnkd', [attn_weights, v])

        y  = x1 + x2
        return self.out_proj(y)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
