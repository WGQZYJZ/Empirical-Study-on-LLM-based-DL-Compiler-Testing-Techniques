
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(embed_dim=128, num_heads=8)
 
    def forward(self, qk1, v1, k1):
        v3, _ = self.multihead_attention(qk1, k1, k1, need_weights=False)
        output  = (v1 * 0.5).matmul(v3.transpose(-2, -1)) + v1
        return output


# Initializing the model
m = Model()
# Inputs to the model
qk1 = torch.randn(2, 8, 4, 16)
k1 = torch.randn(2, 8, 8, 32)
v1 = torch.randn(2, 8, 8, 32)
