
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(8, 1)
 
    def forward(self, qk):
        v4 = self.multihead_attention(qk[0], qk[2])[0]
        v5 = v4 * 0.5
        v6 = v4 * 0.7071067811865476
        v7 = torch.erf(v6)
        v8 = v7 + 1
        v9 = v5 * v8
        return v9


# Initializing the model
m = Model()

# Inputs to the model
qk = (torch.randn(2, 3, 64, 64), torch.randn(2, 8, 64, 64))
