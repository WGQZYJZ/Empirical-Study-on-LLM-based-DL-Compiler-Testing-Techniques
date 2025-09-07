
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multi_head_attention = torch.nn.MultiHeadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, query, key, value):
        v  = self.multi_head_attention(query, key, value)[0]
        return v


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 32, 512)
key   = torch.randn(16, 8, 512)
value = torch.randn(16, 32, 512)
