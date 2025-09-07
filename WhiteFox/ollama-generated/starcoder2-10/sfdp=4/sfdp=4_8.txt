
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, query, key, value, attn_mask=None):
        vq  = self.attn(query, key, value, attn_mask)[0]
        return vq

# Initializing the model
m  = Model()

# Inputs to the model
v1 = torch.randn(48, 512) # A query tensor with shape (batch size, embedding dimensions)
v2 = torch.randn(48, 512) # A key tensor with shape (batch size, embedding dimensions)
v3 = torch.randn(48, 512) # A value tensor with shape (batch size, embedding dimensions)

