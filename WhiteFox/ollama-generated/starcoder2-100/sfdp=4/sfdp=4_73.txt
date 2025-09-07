

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.empty(3, 4))
        self.key = torch.nn.Parameter(torch.empty(5, 6))
 
    def forward(self, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value tensor
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
query = torch.randn(3, 4)
key = torch.randn(5, 6)
value = torch.randn(7, 8)
attn_mask = torch.full((10, 1), -float('inf')) # Generate a mask that has the same size as the query tensor and is filled with -Inf
attn_mask[:3]  +=  1e9 # Pad the attention mask with 10^9
__output__  = m(value)
 