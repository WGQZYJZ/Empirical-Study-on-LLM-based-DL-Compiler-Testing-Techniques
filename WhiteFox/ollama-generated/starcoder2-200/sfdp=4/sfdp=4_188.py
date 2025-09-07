
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        qk /= math.sqrt(torch.tensor(query.size(-1)).float())
 
        if attn_mask is not None:
            qk += attn_mask
        
        attn_weights = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = torch.matmul(attn_weights, value)  # Compute the dot product of the attention weights and the value tensor
        return output

# Initializing the model
scaled = ScaledDotProductAttention()

