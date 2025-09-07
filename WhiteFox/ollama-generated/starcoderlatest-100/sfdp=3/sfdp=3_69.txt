
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=8, num_heads=8)
 
    def forward(self, qk, v):
        attn_output = self.attn(qk, qk, qk)
        output = (attn_output + 1e-5).transpose(-2, -1) @ v
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(8, 3, 64, 64)
value = torch.randn(8, 3, 64, 64)
