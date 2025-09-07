
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=64, num_heads=1)
 
    def forward(self, query, key, value):
        qk = self.attn(query, key, value)[0] # Apply MultiheadAttention to get the output of this pattern
 
        return qk


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(128, 64, 512)
key = torch.randn(128, 64, 512)
value = torch.randn(128, 64, 512)
