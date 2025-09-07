
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
        qk  = torch.einsum("...ij, ...jk->...ik", (query, key)) / math.sqrt(query.size(-1))
        qk  = qk + attn_mask 
        attn_weight  = torch.softmax(qk, dim=-1)
        output   = torch.einsum("...ik,...kv->...iv", (attn_weight, value))
        return output


# Initializing the model
attn = Attention()

 # Inputs to the model
 
query  = torch.randn(32, 64, 64)
key   = torch.randn(32, 64, 64)
value    = torch.randn(32, 64, 512)
attn_mask     = torch.randint(-1e9, 0., (32, 64, 64))

 # Outputs of the model
__output__  = attn(query, key, attn_mask).shape
 
 