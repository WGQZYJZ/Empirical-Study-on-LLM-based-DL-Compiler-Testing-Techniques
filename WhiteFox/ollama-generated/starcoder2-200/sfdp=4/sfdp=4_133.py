
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=None):
        super().__init__()
 
        self.scale = 1 / math.sqrt(dim) if dim else None
 
    def forward(self, query, key, value, attn_mask=None):
        attn_weights = torch.matmul(query, key.transpose(-2, -1)) * \
            self.scale
        
        # Compute the dot product of the query and key tensors
        # Scale the result by 1 / sqrt(dim) (Optional).
 
        # Apply the attention mask to the dot product of the query and key tensors
        if attn_mask is not None:
            attn_weights += attn_mask
            
        # Compute the softmax of the resulting matrix
        attn_weights = torch.softmax(attn_weights, dim=-1)
        
        # Compute a weighted sum of the value tensor by multiplying it with the 
        # attention weights that were computed above.
        output  = torch.matmul(attn_weights, value)
        return output
 
# Initialize the scaled dot-product attention mechanism
m = ScaledDotProductAttention()

