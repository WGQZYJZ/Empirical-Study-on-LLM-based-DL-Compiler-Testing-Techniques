
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention(embed_dim=256, num_heads=8)
 
    def forward(self, q1, k1, v1):
        attn_weight  = self.attn_layer(q1, k1, v1)[0] # Compute the dot product of query and key (plus an attention mask)
        return attn_weight
 
# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(8, 256, 3, 64)
key    = torch.randn(8, 256, 1024, 128)
value  = torch.randn(8, 256, 1024, 128)
