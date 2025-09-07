
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
 
    def forward(self, query):
        key  = None # Set to None when using scaled dot-product attention
        attn_mask = None # Set the mask here (make sure it is not None for self-attention)
        
        v1, v2  = self.attn(query, key=key, attn_mask=attn_mask) 
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
q = torch.randn(8, 3074, 128)
 
# Outputs of the model
__output__  = m(q)

