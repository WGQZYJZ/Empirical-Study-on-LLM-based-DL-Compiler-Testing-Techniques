
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk = torch.matmul(query, key.transpose(-2,-1))/ math.sqrt(key.size(-1)) # Compute the dot product of the query and key tensor
        if attn_mask is not None:
            qk  += attn_mask  # Add the attention mask to the scaled dot-product

        weights = torch.softmax(qk, dim=-1) 
        output = torch.matmul(weights, value) # Compute the weighted sum of the value tensor using the attention weights
        return output

# Initializing the model
m  = ScaledDotProductAttention()

