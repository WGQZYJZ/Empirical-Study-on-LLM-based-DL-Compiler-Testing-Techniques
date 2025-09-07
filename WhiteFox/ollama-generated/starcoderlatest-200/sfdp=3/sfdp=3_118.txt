
class Model(torch.nn.Module):
    def __init__(self, num_heads):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=1)
 
    def forward(self, q1, k1, v1):
        result = self.attention(q1, k1, v1)[0]
        return result

# Initializing the model
m = Model(2)

# Inputs to the model
q1 = torch.randn(1, 3, 64, 64)
k1 = torch.randn(1, 2, 64, 64)
v1 = torch.randn(1, 8, 64, 64)
