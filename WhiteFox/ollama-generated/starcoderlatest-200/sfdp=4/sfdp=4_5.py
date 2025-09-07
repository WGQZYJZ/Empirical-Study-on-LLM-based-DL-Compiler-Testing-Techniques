
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, qk, v):
        attn_weight = self.attn(qk, k=v, v=v)[0]  # Apply multi-head attention on query tensor and key tensor
        return attn_weight


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(16, 4, 8)
v = torch.randn(16, 4, 32)
