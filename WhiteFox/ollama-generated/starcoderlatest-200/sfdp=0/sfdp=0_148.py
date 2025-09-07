
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 2)
 
    def forward(self, x1, x2, mask=None):
        v1 = self.attn(x1, x2, x2)[0]
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 8) # (batch_size=256, n_heads=8, len_query=8, dim_head=32)
x2 = torch.randn(256, 8) # (batch_size=256, n_heads=8, len_key=8, dim_head=32)
