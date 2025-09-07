
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=256, num_heads=1)
 
    def forward(self, qk):
        softmax_qk, attn  = self.attn(q, k)
        return softmax_qk, attn


# Inputs to the model
query = torch.randn(3, 32, 512)
key = torch.randn(3, 64, 512)
