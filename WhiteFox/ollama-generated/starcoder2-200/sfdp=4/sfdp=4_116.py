
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: Tensor, key: Tensor) -> Tensor:
 
        # Compute the dot product of the query and key tensors
        v1 = query @ key.transpose(-2, -1)
 
        # Scale it by the square root of the size of the last dimension of the query tensor (usually 50)
        v2 = v1 / torch.sqrt(query.size(-1))
 
        attn_mask = torch.randn([v2.shape[-2], v2.shape[-1]])  # Attention Mask
        attn_mask[:, :v2.shape[1]] = -10e9   # Use negative infinity to prevent attending to positions that have already been attended to in previous steps
 
        v3 = v2 + attn_mask
 
         # Apply softmax to the scaled dot product
        attn_weights  = torch.softmax(v3, dim=-1) 
        output  = attn_weights @ value
 
 
        return output
