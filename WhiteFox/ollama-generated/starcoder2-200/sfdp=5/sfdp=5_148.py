class SelfAttention(torch.nn.Module):
    def __init__(self, dim: int = 64) -> None:
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask=None, dropout_p=0.1):
        dim_per_head = 8
        head_num = int(dim / dim_per_head)
 
        # Compute the dot product of the query and key, and scale it
        k  = key.transpose(-2,-1)
        v  = value * math.sqrt(query.size(-1))
        attn  = torch.matmul(query @ v, k)
        attn += (attn_mask if attn_mask is not None else torch.zeros(*attn.size()).to(attn.device)).to(attn.dtype)
 
        # Apply softmax to the result and scale it back
        attn /= dim_per_head
        attn = torch.softmax(attn, -1)
 
        # Apply dropout to the softmax output
        attn  = torch.dropout(attn, p=dropout_p, training=self._training)
 
        # Compute the dot product of these attention weights and the value
        out  = (attn @ v).contiguous()
        return out
