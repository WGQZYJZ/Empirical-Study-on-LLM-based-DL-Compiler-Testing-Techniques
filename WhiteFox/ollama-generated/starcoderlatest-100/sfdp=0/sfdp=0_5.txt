
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q, k, v):
        # Apply scaled dot product attention over `query` and `key`.
        x = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.size(-1))

        return x  # Shape [batch_size, heads, head_dim, seq_len]


class TransformerBlock(torch.nn.Module):
    def __init__(self,
                 embed_dim,
                 num_heads,
                 ff_dim,
                 dropout=0.1):
        super().__init__()
        self.attn = ScaledDotProductAttention()

        # Multi-Head attention layer
        self.layer_norm_q = torch.nn.LayerNorm(embed_dim)
        self.self_attn_layer_norm = torch.nn.LayerNorm(embed_dim)
        self.dropout1 = torch.nn.Dropout(p=dropout)

        self.ffn = torch.nn.Sequential(
            torch.nn.Linear(embed_dim, ff_dim),  # Feed Forward Layer
            torch.nn.ReLU(),                         # Non-linear Activation Function
            torch.nn.Linear(ff_dim, embed_dim),     # Second-Layer Feed Forward Network
            torch.nn.Dropout(dropout)                  # Dropout
        )

        self.layer_norm_kv = torch.nn.LayerNorm(embed_dim*2)
        self.dropout2 = torch.nn.Dropout(p=dropout)

    def forward(self, x):
        attn = self.attn(x, x, x)
        output = self.layer_norm_q(x + self.dropout1(attn))

        ffn = self.ffn(output)
        output = self.layer_norm_kv(output + self.dropout2(ffn))

        return output


class Transformer(torch.nn.Module):
    def __init__(self,
                 embed_dim,
                 num_heads,
                 ff_dim,
                 depth,
                 dropout=0.1):
        super().__init__()
        layer = torch.nn.TransformerEncoderLayer(d_model=embed_dim, nhead=num_heads)
        self.transformer = torch.nn.TransformerEncoder(encoder_layer=layer, num_layers=depth)

    def forward(self, x):
        # Apply the multi-head attention module over all of `x` to generate a weighted sum.
        out = self.transformer(x)

        return out


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = TransformerBlock(32, 16, 32, 0.5)
        self.decoder = TransformerBlock(64, 32, 16, 0.5)

    def forward(self, x1):
        # The input of the decoder should be the output of the encoder.
        # Concatenate the first and second outputs to produce an input for the next layer.
        out1 = self.encoder(x1[:, :, :-1, :])
        out2 = torch.cat((out1, x1[:, :, -1:, :]), dim=-2)

        out = self.decoder(out2)  # This should be the output of the model.

        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
