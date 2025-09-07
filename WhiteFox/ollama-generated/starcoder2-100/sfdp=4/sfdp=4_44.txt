
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, q, k, v, attn_mask=None):

        # Compute the dot product of the query and key tensors (without scaling).
        d = torch.matmul(q, k.transpose(-2, -1))
        if attn_mask is not None:
            # Add a mask to the result to zero out attention over padding positions.
            d = d + attn_mask

        # Apply softmax to the result and compute a weighted sum of the value tensor (without scaling).
        attn_weight  = torch.softmax(d, dim=-1)
        
        # Compute the dot product of the attention weights and the value tensors.
        output  = torch.matmul(attn_weight, v)

        return output
