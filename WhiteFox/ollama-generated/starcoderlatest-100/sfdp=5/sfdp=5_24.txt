
class TransformerModel(torch.nn.Module):
    def __init__(self, embed_dim, depth, heads, mlp_ratio, qkv_bias=True, attn_dropout=0., drop_rate=0., num_layers=6, layer_norm_eps=1e-5,
                 activation="gelu", norm_layer=None):
        super().__init__()
 
        # Embedding layers (input: x), position embeddings (input: position) and output projection (input: attn_output)
        self.embedding = nn.ModuleList([nn.Embedding(x, embed_dim) for x in range(depth)])  # embedding size is depth

        # Self-attention module
        self.encoder_attns = nn.ModuleList([TransformerLayer(embed_dim, heads, mlp_ratio, qkv_bias=qkv_bias,
                                                             attn_dropout=attn_dropout, drop_rate=drop_rate) for _ in range(num_layers)])

        # Feedforward module
        self.ffn = nn.ModuleList([nn.Linear(embed_dim, embed_dim),
                                  TransformerLayer(embed_dim, heads, mlp_ratio, qkv_bias=qkv_bias,
                                                             attn_dropout=attn_dropout, drop_rate=drop_rate)])

        # Position-wise Feedforward module (FFN)
        self.ffn_pos = nn.ModuleList([nn.Linear(embed_dim, embed_dim),
                                      TransformerLayer(embed_dim, heads, mlp_ratio, qkv_bias=qkv_bias,
                                                             attn_dropout=attn_dropout, drop_rate=drop_rate)])

        # Layer norm layers
        self.layer_norm = nn.ModuleList([nn.LayerNorm(embed_dim, eps=layer_norm_eps) for _ in range(num_layers)])
 
    def forward(self, x):
        out = [x]
        
        # Embedding and Position Encoding (input: x)
        for i in range(len(self.embedding)):
            pos_enc = torch.unsqueeze(torch.arange(0, self.max_seq_length), 1).repeat(1, self.num_heads, 1, self.seq_length)
            out += [pos_enc]
            x = (self.layer_norm[i](x + self.embedding[i](x)) * math.sqrt(embed_dim)).add_(positional_encodings[:, :, i].unsqueeze(2))
        
        # Transformer Blocks (input: [x, pos_enc])
        for i in range(len(self.encoder_attns)):
            x = out[0] + self.encoder_attns[i](x, x)
            x = self.layer_norm[i+1](x).add_(out[i+1]).relu_()
        
        # FFN (input: [x, pos_enc])
        for i in range(len(self.ffn)):
            y = out[0] + self.ffn[i](x)  # FFN input is the output of each layer of the Transformer model
            z = x.relu_() + y.mul_(y).sub(1.).sigmoid()
            x = (out[0] - x * z).add_(self.layer_norm[len(self.encoder_attns)+i+2](x)).relu_()
        
        # FFN Position (input: [x, pos_enc])
        for i in range(len(self.ffn_pos)):
            y = out[0] + self.ffn_pos[i](x)  # FFN input is the output of each layer of the Transformer model
            z = x.relu_() + y.mul_(y).sub(1.).sigmoid()
            x = (out[0] - x * z).add_(self.layer_norm[len(self.encoder_attns)+len(self.ffn) + i+2](x)).relu_()
            
        return x  # Final output of the model
class TransformerLayer(nn.Module):
    def __init__(self, dim=64, heads=8, mlp_ratio=0., qkv_bias=True,
                 attn_dropout=0., drop_rate=0., num_layers=2,
                 layer_norm_eps=1e-5, activation="gelu", norm_layer=None):
        super().__init__()
 
        # Attention module
        self.attn = nn.MultiheadAttention(embed_dim, heads, qkv_bias=qkv_bias)  # the shape of the input is [bs, seq_len, embed_dim]
        # Feedforward module (FFN: [bs, seq_len, dim])
        self.ffn = nn.Sequential(OrderedDict([
            ("fc1", nn.Linear(embed_dim, int(embed_dim*mlp_ratio))),
            ("act", _get_activation_fn(activation)),
            ("fc2", nn.Linear(int(embed_dim*mlp_ratio), embed_dim)),
        ]))
 
        # Position-wise Feedforward module (FFN: [bs, seq_len, dim])
        self.ffn_pos = nn.Sequential(OrderedDict([
            ("fc1", nn.Linear(embed_dim, int(embed_dim*mlp_ratio))),
            ("act", _get_activation_fn(activation)),
            ("fc2", nn.Linear(int(embed_dim*mlp_ratio), embed_dim)),
        ]))
 
    def forward(self, x:)
- 0.4:  59     -       344     (619287):      54     75          354913  291640  53    61   65    692     146842
