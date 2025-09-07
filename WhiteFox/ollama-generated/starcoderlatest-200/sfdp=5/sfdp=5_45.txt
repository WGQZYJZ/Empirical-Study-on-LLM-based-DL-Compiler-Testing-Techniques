
class Model(torch.nn.Module):
    def __init__(self, embed_dim=128):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads=8)
 
    def forward(self, x1, x2, x3):
        output  = self.attn(x1, x2, x3)[0] # Compute attention based on query, key and value
        return output

# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 x2 = torch.randn(1, 8, 64, 64)
 x3 = torch.randn(1, 64, 32, 32)
