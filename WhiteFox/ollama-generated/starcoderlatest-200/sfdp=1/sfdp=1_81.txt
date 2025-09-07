
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=1024, num_heads=8)
 
    def forward(self, x1, x2):
        a1, (h, _)  = self.attn(x1, x2, x2)
        return h
 
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_0 = SelfAttention()
 
    def forward(self, q, k, v):
        l1  = self.layer_0(q, k)
        return l1

 # Inputs to the model
query  = torch.randn(32, 1024, 64, 64)
key  = torch.randn(32, 1024, 64, 64)
value = torch.randn(32, 1024, 64, 64)
