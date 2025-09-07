
class Model(torch.nn.Module):
    def __init__(self, d_model, heads=128, dropout_p=0.1):
        super().__init__()
        self.heads = heads # Number of heads in multi-head attention
        self.attention_dropout = torch.nn.Dropout(dropout_p)
        self.attention = torch.nn.MultiheadAttention(d_model, heads=heads, dropout=attn_dropout) 
        self.layer_norm = torch.nn.LayerNorm(d_model, eps=1e-6)
 
    def forward(self, x1):
        qk = (self.attention(x1, x1, x1))[0] # attention returns a tuple: output attn, output memory, output query
        qk = self.layer_norm(qk + x1)
        return x1 * 0.5


# Initializing the model
m = Model(d_model=256, heads=16)

# Inputs to the model
x1 = torch.randn(8, 16, 256)
