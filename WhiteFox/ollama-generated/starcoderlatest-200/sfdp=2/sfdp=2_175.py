
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, q, k, v, x):
        attention = self.attention(q, k, v, attn_mask=None)
        return attention[0]

# Inputs to the model
x1 = torch.randn(64, 3, 512) # batch size, embed dim, sequence length
q  = x1[:64]
k  = x1[:64]
v  = x1[:64]
