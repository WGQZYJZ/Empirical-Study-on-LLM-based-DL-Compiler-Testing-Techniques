
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(16, 8)
 
    def forward(self, q1, k1, v1):
        attn_weights = self.attention(q1, k1, v1)[0]
        output = torch.matmul(attn_weights, v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(32, 8, 64, 64)
k1 = torch.randn(32, 8, 64, 64)
v1 = torch.randn(32, 8, 64, 64)
