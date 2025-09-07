
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(embed_dim=768, num_heads=12)
 
    def forward(self, query, key, value, attn_mask=None):
         attn_out = self.attn(query, key, value, attn_mask)
         return attn_out[0]

# Initializing the model
m  = Model()

 # Inputs to the model
query = torch.randn(128, 768).float()
key   = torch.randn(128, 768).float()
value = torch.randn(128, 768).float()

 # Attention mask that is used to prevent self-attention and causality from information flowing backward.
mask = (torch.triu(torch.ones((query.size(-2), query.size(-1))), diagonal=1) == 0).unsqueeze(1)
 
 __output__  = m(query, key, value, mask)
 

