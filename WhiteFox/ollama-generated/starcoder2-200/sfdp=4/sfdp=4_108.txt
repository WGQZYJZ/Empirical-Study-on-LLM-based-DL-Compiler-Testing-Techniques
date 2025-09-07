

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
 
        # Compute the dot product of the query and key tensors
        attn = torch.matmul(query, torch.transpose(key, -2, -1))
 
       # Divide by sqrt of the dimension size of the key tensor
        attn /= math.sqrt(key.size(-1))
 
        # Add an attention mask to the scaled dot product
        attn += attn_mask
 
        # Compute the softmax over the attention weights
        attn_weights = torch.softmax(attn, dim=-1)
 
        # Multiply the value by the attention weights
        output = torch.matmul(attn_weights, value)
 
        return output
