
class MultiHeadAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask):
        # Compute the dot product of the query and key tensors divided by sqrt(query.size(-1))
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
 
        # Add the attention mask to the scaled dot-product
        qk  = qk + attn_mask
 
        # Apply softmax to the result
        attn_weights  = torch.softmax(qk, dim=-1)
 
        # Compute the weighted sum of the value tensor using the attention weights
        output  = attn_weights @ value
 
        return output


# Initializing the model
attn  = MultiHeadAttention()

# Attention masks to mask out certain positions in query and key tensors. It is important that these masks are not hard coded, but should be randomly generated so that the model contains more diversity during inference.
attn_mask1  = torch.randn(32) > 0.5
attn_mask2  = torch.randint(low=0, high=24, size=(64)) == 0


# Inputs to the model
q1  = torch.randn(64, 8, 90)
k1  = torch.randn(37, 8, 90)
v1  = torch.randn(52, 8, 12)
 
attn_mask1  = attn_mask1.repeat((8, 1))  # Broadcast the masks over the batch dimension
attn_mask2  = attn_mask2.repeat((4096,))  # Use one-hot encoding to broadcast the mask across the batch and sequence dimensions
 
__output__  = attn(q1, k1, v1, attn_mask1)

