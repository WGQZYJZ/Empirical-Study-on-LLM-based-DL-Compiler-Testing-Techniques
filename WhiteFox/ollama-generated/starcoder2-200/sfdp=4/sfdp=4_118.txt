
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk  = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        if attn_mask is not None:
            qk  = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = attn_weight @ value # Compute the dot product of the attention weights and the value 
        return output


# Initializing the model
m = Model()
 
# Inputs for the model: query, key, value and optional mask. All these inputs are tensors with shape [1024 x 64]
q_input = torch.randn(1024, 64)
k_input = torch.randn(1024, 384)
v_input = torch.randn(1024, 576)
 
# Optional mask for the model (can be None if not used.)
attn_mask = torch.ones([1024-128, 1024], device=q_input.device, dtype=q_input.dtype)
attn_mask[0:127] = -torch.inf
 
__output__  = m(q_input, k_input, v_input, attn_mask)

