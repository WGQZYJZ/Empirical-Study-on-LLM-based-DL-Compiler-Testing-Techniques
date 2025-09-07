
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention(embed_dim=8, num_heads=1)
 
    def forward(self, x1, x2):
        _, attn_weight  = self.attn_layer(x1, x2, x2)
        output = torch.matmul(attn_weight, x2)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
x2 = torch.randn(8, 8, 64, 64)
