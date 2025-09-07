
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q: Tensor, k: Tensor, v: Tensor, attn_mask: Tensor = None) -> Tuple[Tensor]:
        # Compute dot product between query and key. We scale it to prevent
        # vanishing gradient.
        d = 1 / math.sqrt(q.size(-1))
 
        qk = torch.bmm(q, k.transpose(-2, -1)) * d
 

        if attn_mask is not None:
            attn_mask = attn_mask.repeat(q.size(0), 1, 1)
            qk.masked_fill_(attn_mask, float("-inf"))
        qk = torch.softmax(qk, dim=-1)
 
        # Compute the dot product of the attention weights and value tensor.
        output = attn_weight @ v 
        return output

# Initializing the model