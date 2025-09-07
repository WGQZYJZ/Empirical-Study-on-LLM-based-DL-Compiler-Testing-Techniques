
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(64, 8)
 
    def forward(self, q1, k1, v1, attn_mask=None):
 
        v2, attn_weights  = self.attn(q1, k1, v1, need_weights=True)
        return (v2 + 3) / 5


# Initializing the model
m  = Model()

 # Inputs to the model
q1  = torch.randn(64, 8, 64)
k1  = torch.randn(64, 7, 64)
v1  = torch.randn(64, 5, 64)
attn_mask  = torch.zeros((5, 3))

 # Initializing the model with inputs
__output___= m(q1, k1, v1, attn_mask)
