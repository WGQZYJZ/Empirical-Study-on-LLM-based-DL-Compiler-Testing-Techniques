
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=1, num_heads=8)
 
    def forward(self, xq, xk):
        qk = self.attn(xq, xk, xk)[0]
        return qk


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 32, 64)
x2 = torch.randn(1, 16, 16, 64)
