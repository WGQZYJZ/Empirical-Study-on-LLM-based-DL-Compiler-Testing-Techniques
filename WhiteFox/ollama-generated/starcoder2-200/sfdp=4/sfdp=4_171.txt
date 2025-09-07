
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask=None) -> torch.Tensor:
        attn = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) 
        if attn_mask is not None:
            attn += attn_mask 
        attn_weight = torch.softmax(attn, dim=-1)
        output = attn_weight @ value
 
        return output

m  = ScaledDotProductAttention()

