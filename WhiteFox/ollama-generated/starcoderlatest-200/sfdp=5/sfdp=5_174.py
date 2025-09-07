
class Model(torch.nn.Module):
    def __init__(self, dim_key):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim_query=dim_key)
 
    def forward(self, x1, x2, attn_mask):
        v6, _ = self.attn(x1, x2, x2, key_padding_mask=attn_mask)
        return v6


# Initializing the model
m = Model(dim_key=8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
attn_mask = torch.zeros(1, 3, 64, 64).bool()
