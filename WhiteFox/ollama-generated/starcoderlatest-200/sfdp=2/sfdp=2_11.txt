
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(1, 8, 2)
 
    def forward(self, qk):
        v1, v2 = self.attn(qk, qk, qk)
        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 16, 64, 64)
