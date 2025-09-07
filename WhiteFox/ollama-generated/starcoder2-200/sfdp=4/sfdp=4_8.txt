
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
 
    def forward(self, q1, k1, v1, attn_mask=None)  # Computes the scaled dot product attention
        qlen = q1.size(-2)
        vlen = v1.size(-2)

        qk1 = torch.einsum('...j,...i->...ji', [q1] * (vlen//qlen), [k1]) / math.sqrt(q1.size(-1))
        qk1 += attn_mask  # Add the attention mask to the scaled dot product

        attn_weights = torch.softmax(qk1, dim=-2)  # Apply softmax to the result (divide by qlen)
 
        output = torch.einsum('...ji,...j->...i', [attn_weights] * vlen, [v1])
        return output


# Initializing the model
sdpatt = ScaledDotProductAttention()

# Inputs to the model
x1, x2, x3  = torch.randn(500, 768), torch.randn(500, 768), torch.randn(500, 768)
attn_mask  = (torch.rand(500, 768) > 0.2).to(torch.int32).unsqueeze(-2).repeat(1, 1, 1).permute(2, 0, 1)
out = sdpatt(x1, x2, x3, attn_mask=attn_mask)

