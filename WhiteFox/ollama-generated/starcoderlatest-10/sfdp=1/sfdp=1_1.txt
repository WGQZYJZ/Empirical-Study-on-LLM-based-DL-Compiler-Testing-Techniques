
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 8)
 
    def forward(self, q1, k1, v1):
        v2 = self.attention(q1, k1, v1)[0]
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64)
y1 = torch.randn(1, 8, 64)
z1 = torch.randn(1, 8, 64)
