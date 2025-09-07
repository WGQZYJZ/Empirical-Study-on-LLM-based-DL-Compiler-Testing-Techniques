
class Model(torch.nn.Module):
    def __init__(self, num_heads, dim_kv, num_attns, dim_ffn, dpr=0., use_res_connect=True):
        super().__init__()
        self.dim_q = 16
        self.dim_kv = 32
        self.num_heads = 8

        if dpr == 0:
            dpr = None
    
        self.attn = nn.MultiheadAttention(self.dim_q, self.dim_kv, num_heads=self.num_heads)
        self.pos_ffn = nn.Sequential(nn.Linear(self.dim_kv * 2, dim_ffn),
                                     nn.ReLU(),
                                     nn.Dropout(dpr)) if dpr is not None else None
        self.norm_attn = nn.LayerNorm([self.num_heads, self.dim_kv])

        self.use_res_connect = use_res_connect
        if use_res_connect:
            self.norm_after_attn = nn.LayerNorm(dim_kv)

    def forward(self, x):
        # (bsz, num_attns, seq_len, dim_q) -->> (num_heads * bsz, q_seq_len, dim_k), (num_heads * bsz, q_seq_len, dim_v)
        y, _ = self.attn(x, x, x)

        # Add the attention mask to the scaled dot product at each position in batch and time dimension.
        # This mask is only applied to the final softmax layer when a single query-key pair is used for all instances.
        if self.attn.mask_future:
            y *= torch.arange(y.shape[-1]) < self.attn.cache_past_key

        # (num_heads * bsz, q_seq_len, dim_kv) -->> (bsz, num_attns, seq_len, dim_kv)
        y = y.transpose(0, 1).reshape((-1,) + y.shape[-3:])

        if self.pos_ffn is not None:
            # [dim_q * num_heads] -->> [dim_q]
            y = y.reshape(-1, y.size(-2), y.size(-1))
            y = torch.cat((y, self.norm_attn(y)), dim=-1)
            y = self.pos_ffn(y)
        else:
            y = self.norm_attn(y)

        if self.use_res_connect and (self.pos_ffn is not None):
            y += x
        
        return y  # (bsz, num_attns, seq_len, dim_kv), (bsz, num_attns, seq_len, dim_v)


# Initializing the model
m = Model(num_heads=8, dim_kv=32, num_attns=2, dim_ffn=16)

# Inputs to the model
x = torch.randn(1, 2, 50, 50)
