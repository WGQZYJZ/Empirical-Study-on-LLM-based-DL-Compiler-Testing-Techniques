
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2):
        qk, _ = self.attn(x1, x2)
        v = qk * 0.5 + qk * 0.7071067811865476 + qk
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = torch.randn(2, 3, 64, 64), torch.randn(2, 3, 64, 64)
