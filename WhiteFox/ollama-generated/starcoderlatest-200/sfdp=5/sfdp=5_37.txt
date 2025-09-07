
class Model(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, mlp_ratio=4., qkv_bias=False, qk_scale=None, drop_rate=0., attn_drop_rate=0.,
                 drop_path_rate=0., norm_layer=nn.LayerNorm):
        super().__init__()
        self.norm1 = norm_layer(embed_dim)
        self.attn = nn.MultiheadAttention(embed_dim, num_heads, qkv_bias, qk_scale)
        self.drop_path = StochasticDepth(drop_path_rate)
        
        self.norm2 = norm_layer(embed_dim)
        mlp_hidden_dim = int(embed_dim * mlp_ratio)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, mlp_hidden_dim),
            nn.GELU(),
            nn.Dropout(attn_drop_rate),
            nn.Linear(mlp_hidden_dim, embed_dim),
            nn.Dropout(drop_rate)
        )
        
    def forward(self, x):
        v = self.norm1(x)
        attn_weight, _ = self.attn(v, v, v, None)
        out1 = x + attn_weight * self.drop_path(attn_weight)
        
        out2 = self.drop_path(self.mlp(self.norm2(out1)))
        return out2


# Initializing the model
m = Model(...)

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
