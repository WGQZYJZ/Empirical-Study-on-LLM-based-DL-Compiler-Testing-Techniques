
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2, mask1, mask2):
        qk = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1)) + mask2 # Compute the dot product of the query and key, and scale it
        v1, attn_weight  = self.attn(qk, x2, x2, value=None, key_padding_mask=mask1) # Apply multi-head attention to get qk and attention weights
        return v1


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(4, 3, 64, 64)
mask1 = x1 != 0
mask2 = x2 != 0
