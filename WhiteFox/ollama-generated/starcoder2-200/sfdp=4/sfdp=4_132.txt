
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        # Compute the scaled dot product of the query and key tensors
        qk = torch.bmm(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        if attn_mask is not None:
            qk += attn_mask
        # Apply softmax to the scaled dot product
        attn_weight = F.softmax(qk, dim=-1) 
        output  = torch.bmm(attn_weight, value)

        return output

m  = ScaledDotProductAttention()
__output__  = m(x1)