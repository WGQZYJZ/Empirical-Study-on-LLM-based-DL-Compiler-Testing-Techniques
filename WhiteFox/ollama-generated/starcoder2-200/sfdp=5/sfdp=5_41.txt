
class Transformer(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, qkv_bias=False, qk_scale=None):
        super().__init__()
 
        self.pos_encoding = PositionalEncoding(embed_dim)
 
        self.to_qkv = torch.nn.Linear(embed_dim, 3 * num_heads, bias=qkv_bias)
        self.to_out = torch.nn.Linear(in_features=embed_dim, out_features=embed_dim)
 
        if qk_scale is not None:
            self.qk_scale = qk_scale
        else:
            self.qk_scale = math.sqrt(embed_dim // num_heads)
 
    def forward(self, input): 
        qkv = self.to_qkv(input).reshape(-1, input.shape[-2], 3 * self.num_heads)
 
        # Compute the dot product of the query and key, and scale it
        qk = torch.cat([qkv[0].transpose(-2, -1),
                        qkv[1] @ self.qk_scale,
                        qkv[2]], dim=-1)
 
        qk = qk + self.attn_mask  # Add the attention mask to the scaled dot product
        attn_weights = torch.softmax(qk, dim=-1)
        attn_output = torch.matmul(attn_weights, qkv[-1])
 
        output = self.to_out(torch.cat([attn_output] + qkv[:-1], dim=0))
 
        return output
 
class PositionalEncoding(torch.nn.Module):
    def __init__(self, d_model, dropout=0.2, maxlen=5000):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout)

        # Compute the positional encodings once in log space.
        pe = torch.zeros(maxlen, 1, d_model).to('cuda')
        position = torch.arange(
            maxlen).float().unsqueeze(1)
        div_term = (torch.arange(0., d_model, 2.).float() * (-math.log(
            10000.) / d_model)).exp()
        pe[:, 0, 0::2] = torch.sin(position * div_term)
        pe[:, 0, 1::2] = torch.cos(position * div_term)
        pe.require_grad = False
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + Variable(self.pe[:x.size(0)], requires_grad=False).cuda()

        return self.dropout(x)
