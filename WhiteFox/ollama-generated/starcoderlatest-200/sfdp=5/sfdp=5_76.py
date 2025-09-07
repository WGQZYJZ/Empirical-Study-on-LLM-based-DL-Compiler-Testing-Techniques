
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        attn_weights = self.attention(q1, k1, v1)[0]
        return attn_weights  # Return attention weights


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(2, 3, 64, 64)
k1 = torch.randn(2, 3, 64, 64)
v1 = torch.randn(2, 8, 64, 64)
attn_weights = m(q1, k1, v1)


