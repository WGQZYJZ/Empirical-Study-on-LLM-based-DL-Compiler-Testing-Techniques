
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=32, num_heads=4)
 
    def forward(self, x1, x2, mask=None):
        output, attn_weight = self.attn(x1, x2, x2, need_weights=True)  # Compute the attention weights for every head with `need_weights=True` and store them in a variable called 'attn_weight'
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 32, 64, 64) # Query
x2 = torch.randn(2, 8, 64, 64) # Key
