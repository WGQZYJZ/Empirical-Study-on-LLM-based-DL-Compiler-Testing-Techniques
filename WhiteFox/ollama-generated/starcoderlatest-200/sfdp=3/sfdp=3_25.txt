
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 2, dropout=0.1)
 
    def forward(self, qk_x):
        v1, attn = self.attn(qk_x[0], qk_x[1], qk_x[2])
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64), torch.randn(1, 8, 32, 64), torch.randn(1, 8, 32, 64)
