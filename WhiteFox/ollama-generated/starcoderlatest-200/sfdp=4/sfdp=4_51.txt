
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(12, 3)
 
    def forward(self, query, key, value, attn_mask):
        v4  = self.attn(query, key, value, attn_mask)[0]
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
x2 = torch.randn(8, 12, 64, 64)
x3 = torch.randn(8, 2, 64, 64)
attn_mask = torch.ones((8, 64, 64), dtype=torch.int64)
