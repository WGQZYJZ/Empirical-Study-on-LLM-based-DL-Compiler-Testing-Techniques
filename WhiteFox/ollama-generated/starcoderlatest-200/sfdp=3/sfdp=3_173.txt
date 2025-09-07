
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=16, num_heads=4)
 
    def forward(self, query, key, value):
        qk = self.attn(query, key, value)
        return qk


# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(8, 16, 512, 1024)
key   = torch.randn(8, 32, 512, 1024)
value = torch.randn(8, 32, 512, 1024)
