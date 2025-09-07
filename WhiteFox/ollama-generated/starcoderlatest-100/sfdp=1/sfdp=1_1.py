
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm((3, 64, 64))
        self.attn = torch.nn.MultiheadAttention(32, 8)
 
    def forward(self, x1, x2, query, key, value):
        v1 = self.layer_norm(x2 + self.attn(x1, query, key, output=None, attn_mask=None)[0])
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 32, 64, 64)
x2 = torch.randn(8, 32, 64, 64)
query = torch.randn(32, 32, 64, 64)
key = torch.randn(32, 32, 64, 64)
value = torch.randn(32, 32, 64, 64)
