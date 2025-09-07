
class TransformerEncoderLayer(nn.Module):
    def __init__(self, d_model, heads):
        super().__init__()
        self.d_model  = d_model
        self.heads  = heads
        self.scale  = 1 / math.sqrt(d_model // heads)
 
        self.norm1  = nn.LayerNorm(normalized_shape=d_model)
        self.attn  = MultiHeadAttention(embed_dim=d_model, num_heads=heads)
 
    def forward(self, src):
        output  = self.norm1(src)
        output, _  = self.attn(query=output, key=output, value=output)
​
        return output
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.transformer_encoder  = TransformerEncoderLayer(2560, 14)
 
    def forward(self, x1):
        v1  = self.transformer_encoder(x1)
        return v1


# Initializing the model
m  = Model()
 
# Input to the model
x1  = torch.randn(32, 500)
__output__  = m(x1)

