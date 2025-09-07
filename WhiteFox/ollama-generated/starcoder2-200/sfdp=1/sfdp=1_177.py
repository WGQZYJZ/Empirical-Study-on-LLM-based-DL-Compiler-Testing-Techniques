
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(embed_dim=768, num_heads=12)
 
    def forward(self, query, key, value):
        return self.attn(query, key, value)[0]


# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(32, 64, 768) # Batch size: 32; Sequence length: 64 (for query, key and value tensors).
key  = torch.randn(32, 64, 768)
value  = torch.randn(32, 64, 768)

