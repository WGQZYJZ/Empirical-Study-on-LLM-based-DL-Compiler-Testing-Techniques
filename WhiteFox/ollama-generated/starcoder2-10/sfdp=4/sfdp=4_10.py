
class ScaledDotProductAttention(nn.Module):
    def __init__(self, d_k: int = 0) -> None:
        super().__init__()
 
        self.attn = None
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: Optional[torch.BoolTensor] = None):
        # Compute the scaled dot product of the queries and keys
        dots = (query @ key.transpose(-2, -1)) / math.sqrt(d_k)
 
        if attn_mask is not None:
            dots.masked_fill_(attn_mask == 0, -1e9)
 
       # Apply softmax to the scaled dot product
        self.attn = torch.softmax(dots, dim=-1)
 
        return (self.attn @ value).reshape(-1, query.shape[-2], key.shape[0], d_k)
 
# Initialize the model
scaled_dot_product_attention  = ScaledDotProductAttention()

 # Inputs to the model
query = torch.randn(32, 45, 64)
key   = torch.randn(8192, query.shape[-1])
value = torch.randn(8192, query.shape[0], key.shape[-1])

 # The input tensor must have the same batch dimension and feature dimension as `key` and `value`.
input_tensor  = torch.randn(32, value.shape[0], query.shape[-1])
 
scaled_dot_product_attention(query=query, key=key, value=value)

