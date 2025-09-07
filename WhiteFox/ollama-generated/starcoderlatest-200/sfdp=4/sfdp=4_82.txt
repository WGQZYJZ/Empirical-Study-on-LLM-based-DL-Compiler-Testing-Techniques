
class Self_Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.nn.Parameter(data=torch.zeros((1, 1, 64, 64)), requires_grad=True)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + self.attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
self_attn = Self_Attention()

# Inputs to the model
query = torch.randn(1, 32, 64, 64)
key = torch.randn(1, 32, 64, 64)
value = torch.randn(1, 32, 64, 64)
