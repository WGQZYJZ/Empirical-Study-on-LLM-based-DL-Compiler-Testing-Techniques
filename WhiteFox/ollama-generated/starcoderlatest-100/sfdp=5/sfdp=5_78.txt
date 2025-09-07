
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, qk):
        v1, _ = self.attn(qk, qk, qk, attn_mask=None)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(2, 8, 64, 64)
