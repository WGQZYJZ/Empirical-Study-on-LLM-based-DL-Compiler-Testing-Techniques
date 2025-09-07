
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer  = torch.nn.MultiheadAttention(
            embed_dim, num_heads=num_heads)
 
    def forward(self, query, key, value):
        _, attn_weight  = self.attn_layer(query, key, value,
                                             need_weights=True)
        return attn_weight
# Initializing the model
m = Model()

# Inputs to the model
q1  = torch.randn(2, embed_dim, 512, 368, 4096)  # B x C x Wh x Wd
k1  = torch.randn(2, embed_dim,   3,  256,  256)  # B x C x Kh x Kw x D
v1  = torch.randn(2, embed_dim,  20,  576,   512)  # B x C x Vkh x Vkw x D
