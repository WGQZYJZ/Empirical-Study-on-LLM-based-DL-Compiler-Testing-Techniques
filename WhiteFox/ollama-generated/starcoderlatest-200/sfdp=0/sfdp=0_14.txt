
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
        head_dim = d_model // self.num_heads
        self.scale = head_dim ** -0.5

        self.q_proj = torch.nn.Linear(d_model, num_heads * head_dim)
        self.k_proj = torch.nn.Linear(d_model, num_heads * head_dim)
        self.v_proj = torch.nn.Linear(d_model, num_heads * head_dim)

    def split_heads(self, x):
        x = x.view(-1, x.shape[1], x.shape[2], self.num_heads).permute(0, 3, 1, 2)
        return x

    def forward(self, q, k, v):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / self.scale
        attention_weights = scaled_dot_product.softmax(dim=-1)

        output = attention_weights.matmul(v)
        output = output.permute(0, 2, 3, 1).contiguous()
        new_shape = (attention_weights.shape[0], -1, attention_weights.shape[-1])
        output = output.view(*new_shape)

        return output

class TransformerBlock(torch.nn.Module):
    def __init__(self, ntoken, dim=256):
        super().__init__()
        self.embed_src  = torch.nn.Embedding(ntoken, d_model=dim) # dimension of the input embeddings for the encoder and decoder is the same
        self.layer_norm_1 = torch.nn.LayerNorm(dim)
        self.ff1 = torch.nn.Linear(dim, dim)
        self.dropout = torch.nn.Dropout(p=0.25)
        self.layer_norm_2 = torch.nn.LayerNorm(dim)

        self.attn = MultiHeadAttention(d_model=dim, num_heads=8)
        self.linear = torch.nn.Linear(dim, dim)

    def forward(self, src):
        y = self.attn(src, src, src) + src # Scaled Dot-Product Attention for each input token, a new tensor is obtained for each input token
        z = torch.relu(self.ff1(y)) + y

        return self.layer_norm_2(z), y

class EncoderLayer(torch.nn.Module):
    def __init__(self, ntoken, dim=256):
        super().__init__()
        self.selfattn = TransformerBlock(ntoken, dim)

    def forward(self, src, encdec=None):
        z1, y1 = self.selfattn(src) # First Layer of Multi-Head Attention
        return (z1 + src), y1

class DecoderLayer(torch.nn.Module):
    def __init__(self, ntoken, dim=256):
        super().__init__()
        self.ff = torch.nn.Linear(dim, dim)

        self.layer_norm_self = torch.nn.LayerNorm(dim)
        self.selfattn = TransformerBlock(ntoken, dim)
        self.layer_norm_encdec = torch.nn.LayerNorm(dim)

        if encdec is None:
            return # If encdec tensor is not provided, we just need to use the self-attention

        dec_emb = torch.relu(self.ff(encdec)) # Second Layer of Multi-Head Attention
        self.encattn = TransformerBlock(ntoken, dim)

    def forward(self, src, z2):
        z1, y1 = self.selfattn(src) # First Layer of Multi-Head Attention

        z2 = self.encattn(z2, z2 + y1, encdec) # Second Layer of Multi-Head Attention
        return (z1 + src), z2 + y1

class EncoderBlock(torch.nn.Module):
    def __init__(self, ntoken, dim=256):
        super().__init__()
        self.layer_norm_src = torch.nn.LayerNorm(dim)

        if encdec is None:
            return # If encdec tensor is not provided, we just need to use the self-attention

        self.sublayer = TransformerBlock(ntoken, dim)

    def forward(self, src):
        z1, y1 = self.sublayer(src) # First Layer of Multi-Head Attention

        return self.layer_norm_src(z1 + src), y1

class DecoderBlock(torch.nn.Module):
    def __init__(self, ntoken, dim=256):
        super().__init__()
        self.encattn = EncoderBlock(ntoken)

    def forward(self, src, encdec):
        z1, y1 = self.encattn(src + encdec) # First Layer of Multi-Head Attention

        return (z1 + src), (z1 + encdec)

class TransformerModel(torch.nn.Module):
    def __init__(self, ntoken, nposition, dim=256):
        super().__init__()
        self.encoder = torch.nn.TransformerEncoderLayer(ntoken, dim)
        self.decoder = torch.nn.TransformerDecoderLayer(dim, ntoken, dim)

    def forward(self, src, encdec=None):
        z1 = self.encoder(src)

        if encdec is not None:
            z2 = self.decoder(z #3407464574597555
