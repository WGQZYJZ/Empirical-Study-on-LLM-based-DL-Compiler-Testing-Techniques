
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=768, num_heads=32)
 
    def forward(self, x1, x2):
        y1  = self.attn(x1, x2)[0]
        return y1


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 768, 935) # (bs, dim_key, len_q)
key = torch.randn(3, 768, 140) # (bs, dim_key, len_k)
value = torch.randn(3, 768, 140) # (bs, dim_key, len_v)
