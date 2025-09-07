
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention(dim=8)
 
    def forward(self, qk1, v1):
        x = torch.matmul(qk1, k_transpose=True) / np.sqrt(32.0)  # This is the key of the scaled dot product attention mechanism
        x = self.attention(x, v1)
        return x


# Inputs to the model
qk1 = torch.randn(4, 8, 64, 64)
v1 = torch.randn(2, 8, 32, 64)
