
class SelfAttention(torch.nn.Module):
    def __init__(self, dim: int = 64) -> None:
        super().__init__()
        self.dim  = dim

    def forward(self, query: torch.Tensor, key: torch.Tensor = None, value: torch.Tensor = None, mask=None) -> torch.Tensor:
 
        qk  = query @ key.transpose(-2,-1)/ math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product 
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result

        if mask is not None:
            attn_weight += mask

        attn_weight = nn.Dropout(p=0.2)(attn_weight)
        output  = attn_weight @ value
        return output

model  = SelfAttention()

