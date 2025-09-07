
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, attn_mask: torch.Tensor) -> torch.Tensor:
 
        # Compute the dot product of the query and key
        qk  = torch.matmul(query, key.transpose(-2, -1))
 
        # Scale the result by the square root of the size of the query vector (-1)
        qk /= math.sqrt(query.size()[-1])
 
        
        # Add the attention mask to the scaled dot product
        qk += attn_mask
 
        # Apply softmax to the result
        attn_weights  = torch.softmax(qk, dim=-1)
 
   
        # Compute a weighted sum of the value tensor based on the attention weights 
        output  = torch.matmul(attn_weights, key)

        return output

m  = ScaledDotProductAttention()

q  = torch.randn((48023979, 64))   # Random input for query
k  = torch.randn((512, 512))        # Input for the key matrix
attn_mask  = torch.randn(q.size()) # Attention mask for masked attention
__output__  = m(query=q, attn_mask=attn_mask)

