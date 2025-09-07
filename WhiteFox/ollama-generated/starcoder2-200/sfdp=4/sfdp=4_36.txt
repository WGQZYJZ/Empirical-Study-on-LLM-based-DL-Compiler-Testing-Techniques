
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        v1  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        if not self._ignoreMask:
            v1 += v1
        v2  = torch.softmax(v1, dim=-1) # Apply softmax to the result
        v3  = torch.matmul(v2, value) # Compute the dot product of the attention weights and the value tensor
        return v3
