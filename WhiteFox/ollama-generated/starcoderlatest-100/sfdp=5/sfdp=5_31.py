
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 32)
 
    def forward(self, x1, key, query, value, attn_mask=None):
        v1, attn_weight = self.attn(x1, key, value, attn_mask)
        return v1

# Inputs to the model
qkv = torch.randn(8, 32, 64, 64)
