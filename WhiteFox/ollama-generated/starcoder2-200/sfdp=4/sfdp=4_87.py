
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=768, num_heads=12)
 
    def forward(self, query, key, value, attn_mask):
        v  = self.attn(query=query, key=key, value=value,
                       attn_mask=attn_mask)[0] 
        return v


# Initializing the model
m  = Model()

# Inputs to the model
key   = torch.randn(16384, 768)  # Batch size of the key tensor is set to 16384. 
value = torch.randn(2048, 768)    # Batch size of the value tensor is set to 2048. 
attn_mask = torch.zeros([256, 256]) + -float('inf')
query   = key @ value / math.sqrt(key.size(-1))
attn_mask = attn_mask[:3,:3]


__output__= m(query=query, key=key, value=value, attn_mask=attn_mask)

