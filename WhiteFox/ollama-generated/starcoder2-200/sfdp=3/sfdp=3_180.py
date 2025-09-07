
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(128, 4)
 
    def forward(self, q, k=None, v=None):
        o1, o2, o3 = self.attn(q, key_padding_mask=k, value_padding_mask=v).transpose(-1,-2)
        return o1

# Initializing the model
m  = Model()
 
# Inputs to the model
key  = torch.randn(8, 3200, 64, 64)
query = torch.randn(8, 59900, 32, 32)
v  = None
k  = None
 
