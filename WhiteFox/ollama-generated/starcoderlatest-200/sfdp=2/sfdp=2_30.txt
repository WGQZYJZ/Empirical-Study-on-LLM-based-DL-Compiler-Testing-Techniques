
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 32)
 
    def forward(self, x1, query, key):
        qk = self.attention(x1, query, key, attn_mask=None)[0]
        return qk

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(128, 32, 8)
key   = torch.randn(128, 32, 8)
x1    = torch.randn(128, 8, 64, 64)
