
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, qk, attn_mask, v):
        attn_weight = self.attn(qk, k=v, v=v)[0]
        return attn_weight
 
 # Initializing the model
m = Model()

 # Inputs to the model
qk = torch.randn(1, 4, 5, 8)
attn_mask = torch.randn(1, 5, 64, 64)
v = torch.randn(1, 8, 32, 32)
