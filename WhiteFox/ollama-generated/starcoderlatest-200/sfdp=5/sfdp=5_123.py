
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attn = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, x1, x2):
        qk = self.multihead_attn(x1, x2)[0]  # Compute the dot product of the query and key, and scale it
        return qk


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 512, 64, 64)
x2 = torch.randn(32, 512, 64, 64)
