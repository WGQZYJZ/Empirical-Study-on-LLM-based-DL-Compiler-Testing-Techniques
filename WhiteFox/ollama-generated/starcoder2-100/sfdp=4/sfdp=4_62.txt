
class MultiHeadAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk  = torch.einsum('bmd,dmk->mbn', (query, key)) / math.sqrt(query.size(-1)) + attn_mask
        attn_weight  = torch.softmax(qk, dim=-1)
        output  = torch.einsum('mdn,ndm->mdm', (attn_weight, value))
        return output

# Initializing the model
attn = MultiHeadAttention()


# Inputs to the model
query  = torch.randn(32, 50, 128)
key   = query + 3.0
value = key - 6.0
__output__  = attn(query, key, value)