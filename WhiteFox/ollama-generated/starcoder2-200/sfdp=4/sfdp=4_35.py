
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.Tensor = None) -> Tuple[torch.Tensor]:
        scale  = math.sqrt(query.size(-1))
 
        kq  = query @ key.transpose(-2, -1) / scale
 
#        v = torch.nn.Dropout() (attn_weight)
#        attn_weight += torch.nn.AlphaDropout()

        if attn_mask is not None:
            attn_weight += attn_mask
 
        attn_weight  = torch.softmax(kq, dim=-1)
        return attn_weight @ value, kq


# Initializing the model
m  = ScaledDotProductAttention()

 # Inputs to the model
query = torch.randn(32,  64, 500).detach() + 3.9
key   = torch.randn(32,  8192, 500) / 77 + query
value = torch.randn(32,  8192, 16)

 # Initializing the attention mask
attn_mask  = torch.empty((query.size(0), key.size(-2))).fill_(float('-inf')).detach()
attn_mask[range(query.size(0)), range(key.size(-2))].fill_(3.)
 
# Attention weights
weight, kq  = m(query=query, key=key, value=value, attn_mask=attn_mask)

 