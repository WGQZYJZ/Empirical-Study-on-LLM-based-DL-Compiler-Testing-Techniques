
class Model(torch.nn.Module):
    def __init__(self, n_heads=4):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 2 * n_heads, dropout=0)
 
    def forward(self, x1, x2):
        qk = self.attn(x1, x2)[0]
        output = torch.cat((q1, k2), dim=-1) * v5 
        return output
# Initializing the model
m = Model(4)

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
