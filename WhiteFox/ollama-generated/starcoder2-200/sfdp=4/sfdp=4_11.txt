
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask=None) -> torch.Tensor:
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
 
        if isinstance(attn_mask, torch.nn.modules.module.Module):
            qk += attn_mask()
        else:
            qk += attn_mask
 
        attn_weight = torch.softmax(qk, dim=-1) 
        return attn_weight @ value


# Initializing the model
m  = ScaledDotProductAttention() 

 # Inputs to the model 
query  = torch.randn(2560 ,384) 
key   = query 
value  = key 
attn_mask=None

 