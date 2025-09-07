
class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = torch.nn.Embedding(10, 32)
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key):
        qkv = self.encoder(query @ key.transpose(-2, -1))
        attn_output, attn_weight  = self.attn(qkv, qkv, qkv) # Compute the scaled dot-product attention of the encoder embedding with itself
