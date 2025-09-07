
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(embed_dim=1024, num_heads=16)
 
    def forward(self, q, k, v):
        return self.attn(q, k)[0] * scale + v


# Initializing the model
m  = Model()


# Inputs to the model
q = torch.randn(8, 32, 16)
k = torch.randn(8, 32, 16)
v = torch.randn(8, 32, 1024)
 