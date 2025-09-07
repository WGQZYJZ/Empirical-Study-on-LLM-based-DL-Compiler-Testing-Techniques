
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
 
        # Attention mechanism
        qk = torch.einsum("bijc,bjcd->bdic", (query, key)) / math.sqrt(query.size(-1)) 
        attn_mask  = torch.zeros_like(qk)
        attn_mask.triu_(1)
 
        attn_weight = torch.softmax(attn_mask, dim=-1) 
 
        value = torch.randn((key).shape[0], key.shape[-2], -1)
        output = attn_weight @ value

        return 0


# Initializing the model
m  = Model()

# Inputs to the model
query = torch.randn(4, 3, 64)
key   = torch.randn(4, 3, 128).transpose(-2,-1) # .shape[-2] = key.shape[0], -1 = 128
 
__output__  = m(query, key)