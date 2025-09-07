
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8, dropout=0):
        super().__init__()
        self.num_heads = num_heads
        assert embed_dim % num_heads == 0
        # The embedding layer is the input to both heads
        self.embed_dim = embed_dim
        self.dropout = torch.nn.Dropout(p=dropout)

    def forward(self, qk):
        batch_size = qk.shape[0]
        assert batch_size == key.shape[0] and key.shape[1] == self.embed_dim

        # Split the inputs into heads
        q, k, v = torch.chunk(qk, 3, dim=2)
        assert q.shape == (batch_size, self.num_heads, -1)
        assert k.shape == (batch_size, self.num_heads, -1)
        assert v.shape == (batch_size, self.num_heads, -1)

        # Dot product between heads and keys in a batch of queries
        qk = torch.matmul(q, k.transpose(-2, -1))  # (B x N x Lq x Rk) x (Rky x N x Ey) -> (B x N x Lq x Rk)

        # Scale the dot product to the dimension of keys
        qk = qk / math.sqrt(q.shape[-1])

        # Dot-product attention with heads and apply dropout
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = self.dropout(attn_weight)

        # Weighted sum of the values by attention weights (scaled dot product attention)
        output = torch.matmul(attn_weight, v)  # (B x N x Lq x Rk) x (B x N x Ey x Rk) -> (B x N x Lq x Ey)

        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.embed_dim = 512 # Embedding dimension for each embedding head
        self.num_heads = 8 # Number of attention heads
        self.attn = MultiHeadSelfAttention(self.embed_dim, self.num_heads)
 
    def forward(self, qk):
        output = self.attn(qk)
 
        return output
# Initializing the model
m = Model()


class EncoderLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layernorm1 = torch.nn.LayerNorm(dim=768, eps=1e-6)
        self.self_attn = MultiHeadSelfAttention(embed_dim=768, num_heads=8, dropout=0.2)
        self.linear = torch.nn.Linear(in_features=768, out_features=768)

    def forward(self, x):
        residual = x  # Residual connections start from the input tensor
        x = self.layernorm1(x)

        x = self.self_attn(x)

        x = torch.nn.functional.relu(x)
        x = self.linear(x)

        x = x + residual
        x = torch.nn.functional.relu(x)
 
        return x, residual
 
class Transformer(torch.nn.Module):
    def __init__(self, num_layers=3):
        super().__init__()
        # The transformer encoder is the input to the self-attention module
        self.encoder = torch.nn.TransformerEncoder(EncoderLayer())
        self.decoder = torch.nn.TransformerDecoder(DecoderLayer())

    def forward(x):
        out = self.encoder(x)

        return out
# Initializing the model
m = Transformer()


class EncoderBlock(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8):
        super().__init__()
        self.layernorm1 = torch.nn.LayerNorm(dim=embed_dim, eps=1e-6)
        self.attn = MultiHeadSelfAttention(embed_dim=embed_dim, num_heads=num_heads)
 
    def forward(self, x):
        residual = x  # Residual connections start from the input tensor
        x = self.layernorm1(x)

        x = self.attn(x)

        x = torch.nn.functional.relu(x)
 
        return x, residual
 
class Transformer(torch.nn.Module):
    def __init__(self, num_layers=3):
        super().__init__()
        # The transformer encoder is the input to the self-attention module
        self.encoder1 = EncoderBlock(embed_dim=512)
        self.encoder2 = EncoderBlock(embed_dim=512)
 
    def forward(self, x):
        out = self.encoder1(x)

        out = self.encoder2(out)

        return out
# Initializing the model
m = Transformer()


class DecoderBlock(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8):
        super().__init__()
        # The transformer encoder is the input to the self-attention module
        self.layernorm1 = torch.nn.LayerNorm(dim=embed_dim, eps=1e-6)
        self.attn = MultiHeadSelfAttention(embed_dim=embed_dim, num_heads=num_heads)
        self.layernorm2 = torch.nn.LayerNorm(dim=embeding  self.out_1_000000000
