
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None):
        qk  = torch.bmm(query, key.transpose(-2,-1)) / math.sqrt(key.size(-1)) # Scale the dot product of the query and key tensors to avoid numerical instability
        if isinstance(attn_mask, torch.Tensor):
            attn_mask = attn_mask.to(query.device)
        if isinstance(attn_mask, (int, float)):  # Allow for a scalar mask as an argument for backwards compatibility with previous versions of the API.
            attn_mask = torch.ones((1, qk.size(-2), qk.size(-1)), device=qk.device) * attn_mask
        qk  += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result of the dot product
        output  = attn_weight @ key  # Compute a weighted sum using the attention weights and the value tensor 
        return output

# Initializing the model
m  = Model()

# Inputs for the model
query, key, attn_mask  = torch.randn(8, 32, 64), torch.randn(8, 64, 64), attn_mask = 0 # Attn mask is not used here


__output__  = m(query, key, attn_mask=attn_mask)

